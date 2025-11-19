import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from PIL import Image
import os

# === WINDOWS PATHS ===
save_dir = r"C:\Users\Moona Mridul\Desktop\sepsis"

hist_out = os.path.join(save_dir, "accuracy_hist.png")
roc_out = os.path.join(save_dir, "roc_curve.png")
line_out = os.path.join(save_dir, "accuracy_line_chart.png")
confusion_image_path = os.path.join(save_dir, "download.png")

# === Model Names ===
paper1_name = "Comprehensive Evaluation (RF)"
paper2_name = "Early Sepsis Prediction (RF)"
your_model_name = "Sepsis Hybrid Model"

# === Accuracy Values ===
paper1_best_acc = 77.5
paper2_best_acc = 87.0
your_accuracy_percent = 98.6
your_auc = 0.9376377893045178

# Confusion matrix values
TN = 150242
FP = 1
FN = 2137
TP = 19

# === HISTOGRAM ===
labels = [paper1_name, paper2_name, your_model_name]
accuracies = [paper1_best_acc, paper2_best_acc, your_accuracy_percent]

plt.figure(figsize=(10,6))
bars = plt.bar(labels, accuracies, color=["#6495ED", "#FF8C00", "#32CD32"])
plt.ylabel("Accuracy (%)")
plt.title("Accuracy Comparison Across Papers & Sepsis Hybrid Model")

for bar, acc in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5,
             f"{acc:.1f}%", ha='center', color='white', fontsize=12, fontweight="bold")

plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(hist_out, dpi=150)
plt.show()

print("Saved histogram to:", hist_out)

# === LINE CHART ===
plt.figure(figsize=(10,6))
plt.plot(labels, accuracies, marker="o", linewidth=3, markersize=10, color="#8A2BE2")

for i, acc in enumerate(accuracies):
    plt.text(i, acc + 1, f"{acc:.1f}%", ha="center", fontsize=11, fontweight="bold")

plt.title("Accuracy Trend (Line Chart)")
plt.ylabel("Accuracy (%)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(line_out, dpi=150)
plt.show()

print("Saved line chart to:", line_out)

# === ROC CURVE (Single Point) ===
tpr = TP / (TP + FN)
fpr = FP / (FP + TN)

plt.figure(figsize=(7,7))
plt.plot([0, 1], [0, 1], 'k--', label='Chance')
plt.scatter(fpr, tpr, color='red', s=150,
            label=f"{your_model_name} (TPR={tpr:.3f}, FPR={fpr:.6f})")
plt.title(f"ROC Curve — {your_model_name} (AUC = {your_auc:.4f})")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.grid(True)

plt.savefig(roc_out, dpi=150)
plt.show()

print("Saved ROC curve to:", roc_out)

# === Show confusion matrix image ===
if os.path.exists(confusion_image_path):
    img = Image.open(confusion_image_path)
    plt.figure(figsize=(5,5))
    plt.imshow(img)
    plt.axis('off')
    plt.title("Confusion Matrix (Sepsis Hybrid Model)")
    plt.show()
else:
    print("Confusion matrix image not found:", confusion_image_path)
