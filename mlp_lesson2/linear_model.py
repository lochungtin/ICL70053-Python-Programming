import torch


class ModelNumberQuestions(torch.nn.Module):
    def __init__(self):
        super().__init__()
        initial_theta_0 = torch.Tensor([1])
        initial_theta_1 = torch.Tensor([2])
        self.theta_0 = torch.nn.Parameter(initial_theta_0)
        self.theta_1 = torch.nn.Parameter(initial_theta_1)

    def forward(self, tensor_number_tasks):
        return self.theta_1 * tensor_number_tasks + self.theta_0


def compute_loss(list_number_tasks, list_number_questions, t0, t1):
    mse_loss = torch.Tensor([0])

    for task, question in zip(list_number_tasks, list_number_questions):
        estimator = t1 * task + t0
        mse_loss += (estimator - question) ** 2

    return mse_loss / len(list_number_tasks)


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
    initial_theta_0 = torch.Tensor([1])
    initial_theta_1 = torch.Tensor([2])
    theta_0 = torch.nn.Parameter(initial_theta_0)
    theta_1 = torch.nn.Parameter(initial_theta_1)

    optimiser = torch.optim.SGD([theta_0, theta_1], lr=learning_rate)

    for i in range(number_training_steps):
        optimiser.zero_grad()

        mse_loss = compute_loss(
            list_number_tasks, list_number_questions, theta_0, theta_1
        )
        mse_loss.backward()

        optimiser.step()

    return theta_0, theta_1


list_number_tasks = [1, 2, 4, 4, 5, 6, 6, 6, 8, 8, 9, 10]
list_number_questions = [5, 11, 21, 22, 26, 31, 32, 31, 41, 42, 48, 52]

print(train_parameters_linear_regression(list_number_tasks, list_number_questions))
