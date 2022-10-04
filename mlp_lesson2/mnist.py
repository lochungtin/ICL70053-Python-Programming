import torch
import torchvision
import torchvision.transforms as transforms


def load_training_dataset():
    transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.5), (0.5))]
    )

    trainset = torchvision.datasets.MNIST(
        root="mlp_lesson2/data", train=True, download=True, transform=transform
    )

    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=len(trainset), shuffle=True, num_workers=2
    )

    dataset_training_images, dataset_training_labels = next(iter(trainloader))

    return dataset_training_images, dataset_training_labels


class MNISTClassifier(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=28 * 28, out_features=10)

    def forward(self, tensor_images):
        tensor_images = tensor_images.view(-1, 1 * 28 * 28)
        outcome_scores = self.linear(tensor_images)
        return outcome_scores


load_training_dataset()

mnist_classifier = MNISTClassifier()
n_batch = 42
random_tensor = torch.randn(size=(n_batch, 1, 28, 28))
print(mnist_classifier(random_tensor).size()) 
