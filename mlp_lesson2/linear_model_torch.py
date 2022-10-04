import torch


class ModelNumberQuestions(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=1, out_features=1)

    def forward(self, tensor_number_tasks):
        return self.linear(tensor_number_tasks)


class MSELoss(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()

    def forward(self, estimates, actuals):
        sqr_diff = (estimates - actuals) ** 2
        return sqr_diff.mean()


def train_parameters_linear_regression(
    list_number_tasks,
    list_number_questions,
    learning_rate=0.02,
    number_training_steps=200,
):
    """
    Instantiate ModelNumberQuestions model and optimises the parameters of the model, given the dataset
    of list_number_tasks and list_number_questions.
    Args:
        list_number_tasks (List[float]): of size n where n is the number of questions (it is also the number of tasks)
        list_number_questions (List[float]): of size n where n is the number of questions (it is also the number of tasks)
        learning_rate (float):
        number_training_steps (int):

    Returns:
        trained network (ModelNumberQuestions)
    """
    net = ModelNumberQuestions()
    mse = MSELoss()

    optimiser = torch.optim.SGD(net.parameters(), lr=learning_rate)

    for i in range(number_training_steps):
        optimiser.zero_grad()

        estimates = net(list_number_tasks)
        loss = mse(estimates, list_number_questions)
        loss.backward()

        optimiser.step()

    for param in list(net.named_parameters()):
        print(param)

    return net


list_number_tasks = torch.Tensor([1, 2, 4, 4, 5, 6, 6, 6, 8, 8, 9, 10]).view(-1, 1)
list_number_questions = torch.Tensor(
    [5, 11, 21, 22, 26, 31, 32, 31, 41, 42, 48, 52]
).view(-1, 1)

train_parameters_linear_regression(list_number_tasks, list_number_questions)
