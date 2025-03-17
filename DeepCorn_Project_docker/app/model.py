# model.py
import torch
import torch.nn as nn

class DeepCornModelV2(nn.Module):
    def __init__(self, input_dim, hidden_units, num_layers, dropout_rate):
        super(DeepCornModelV2, self).__init__()

        layers = []
        in_features = input_dim
        
        for _ in range(num_layers):
            layers.append(nn.Linear(in_features, hidden_units))
            layers.append(nn.GELU())
            layers.append(nn.Dropout(dropout_rate))
            in_features = hidden_units

        layers.append(nn.Linear(in_features, 1))

        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)


def load_model(weights_path="DeepCorn_Best_Model_optimized.pth", input_dim=447):
    best_params = {'num_layers': 4, 'hidden_units': 485, 'dropout_rate': 0.407}

    model = DeepCornModelV2(
        input_dim=input_dim,
        hidden_units=best_params['hidden_units'],
        num_layers=best_params['num_layers'],
        dropout_rate=best_params['dropout_rate']
    )
    
    model.load_state_dict(torch.load(weights_path, map_location=torch.device('cpu')))
    model.eval()
    return model

# if __name__== '__main__':
#     model = load_model(input_dim=47)

#     sample_input = torch.randn(1, 47)  # Batch size = 1, Input dimension = 447
#     output = model(sample_input)
#     print(output)
