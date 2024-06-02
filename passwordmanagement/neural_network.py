# import torch
# import torch.nn as nn
# import torch.optim as optim
# import numpy as np
# import secrets
# import string


# # Подготовка набора данных
# # Предположим, что у нас есть список паролей и их меток сложности (0 - низкая, 1 - средняя, 2 - высокая)
# def generate_random_passwords(num_passwords, min_length, max_length):
#     passwords = []
#     for _ in range(num_passwords):
#         length = secrets.choice(range(min_length, max_length + 1))
#         password = "".join(
#             secrets.choice(string.ascii_letters + string.digits + string.punctuation)
#             for _ in range(length)
#         )
#         passwords.append(password)
#     return passwords


# # Преобразование паролей в числовые векторы (например, one-hot encoding)
# def password_to_vector(password, max_length):
#     vector = [0] * max_length

#     for i, char in enumerate(password):
#         if char in string.ascii_letters:
#             index = ord(char.lower()) - ord("a") + 1  # Преобразуем букву в число (1-26)
#         elif char in string.digits:
#             index = ord(char) - ord("0") + 27  # Преобразуем цифру в число (27-36)
#         else:
#             index = 37  # Символы пунктуации и прочие

#         vector[i] = index

#     return vector


# # Функция преобразования метки сложности в one-hot encoding
# def label_to_onehot(label, num_classes):
#     onehot = [0] * num_classes
#     onehot[label] = 1
#     return onehot


# # Создание нейронной сети
# class PasswordClassifier(nn.Module):
#     def __init__(self, input_size, hidden_size, num_classes):
#         super(PasswordClassifier, self).__init__()
#         self.fc1 = nn.Linear(input_size, hidden_size)
#         self.relu = nn.ReLU()
#         self.fc2 = nn.Linear(hidden_size, num_classes)

#     def forward(self, x):
#         out = self.fc1(x)
#         out = self.relu(out)
#         out = self.fc2(out)
#         return out


# input_size = 100  # длина вектора пароля
# hidden_size = 50  # Размер скрытого слоя
# num_classes = 3  # Количество классов (количество уровней сложности паролей)
# model = PasswordClassifier(input_size, hidden_size, num_classes)
# criterion = nn.CrossEntropyLoss()
# optimizer = optim.Adam(model.parameters(), lr=0.001)

# # Обучение нейронной сети
# num_epochs = 10
# for epoch in range(num_epochs):
#     for password, label in zip(password, label):
#         # Преобразование пароля и метки в тензоры PyTorch
#         password_vector = torch.Tensor(password_to_vector(password))
#         label_onehot = torch.Tensor(label_to_onehot(label))

#         # Прямое распространение
#         outputs = model(password_vector)
#         loss = criterion(
#             outputs, torch.Tensor([label])
#         )  # Кросс-энтропия для многоклассовой классификации

#         # Обратное распространение и оптимизация
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#     print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")

# # Сохранение модели
# torch.save(model.state_dict(), "password_classifier.pth")
