This is the implementation of https://github.com/GemsLab/GroupINN on a custom data with 116 rois


Current loss weights: {'cross_entropy': 1.0, 'l2_penalty': 0.002, 'neg_penalty_gnn': 0.2, 
'neg_penalty_reduce': 0.1, 'ortho_penalty_n': 0.2, 'ortho_penalty_p': 0.2, 'variance_penalty_n': 0.5, 
'variance_penalty_p': 0.3} 
Model size: 1.412K 
Number of Epochs:300 
Batch size:16 

Model Performance
Training, Validation, and Test Metrics


Train Set:
Loss: 0.547232
Accuracy: 74.70%
True Positive Rate (TPR): 77.54% (428/552)
True Negative Rate (TNR): 71.85% (393/547)
Precision: 73.54%
Recall: 77.54%
F1 Score: 75.49% (30-epoch avg: 72.17%)


Validation Set:
Loss: 0.752783
Accuracy: 56.10%
True Positive Rate (TPR): 54.84% (34/62)
True Negative Rate (TNR): 57.38% (35/61)
Precision: 56.67%
Recall: 54.84%
F1 Score: 55.74% (30-epoch avg: 52.46%)


Test Set:
Loss: 0.747446
Accuracy: 58.05%
True Positive Rate (TPR): 61.00% (122/200)
True Negative Rate (TNR): 54.05% (80/148)
Precision: 64.21%
Recall: 61.00%
F1 Score: 62.56% (30-epoch avg: 60.22%)
