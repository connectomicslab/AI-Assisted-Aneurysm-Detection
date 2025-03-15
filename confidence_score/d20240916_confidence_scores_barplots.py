import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def plot_confidence_barplot(tp_confidence_junior_assisted_mean_std,
                            tp_confidence_junior_unassisted_mean_std,
                            fp_confidence_junior_assisted_mean_std,
                            fp_confidence_junior_unassisted_mean_std,
                            tp_confidence_senior_assisted_mean_std,
                            tp_confidence_senior_unassisted_mean_std,
                            fp_confidence_senior_assisted_mean_std,
                            fp_confidence_senior_unassisted_mean_std):
    # Data preparation
    labels = ['Junior', 'Senior']

    tp_assisted_means = [tp_confidence_junior_assisted_mean_std[0], tp_confidence_senior_assisted_mean_std[0]]
    tp_assisted_stds = [tp_confidence_junior_assisted_mean_std[1], tp_confidence_senior_assisted_mean_std[1]]

    tp_unassisted_means = [tp_confidence_junior_unassisted_mean_std[0], tp_confidence_senior_unassisted_mean_std[0]]
    tp_unassisted_stds = [tp_confidence_junior_unassisted_mean_std[1], tp_confidence_senior_unassisted_mean_std[1]]

    fp_assisted_means = [fp_confidence_junior_assisted_mean_std[0], fp_confidence_senior_assisted_mean_std[0]]
    fp_assisted_stds = [fp_confidence_junior_assisted_mean_std[1], fp_confidence_senior_assisted_mean_std[1]]

    fp_unassisted_means = [fp_confidence_junior_unassisted_mean_std[0],
                           fp_confidence_senior_unassisted_mean_std[0] if fp_confidence_senior_unassisted_mean_std else 0]
    fp_unassisted_stds = [fp_confidence_junior_unassisted_mean_std[1],
                          fp_confidence_senior_unassisted_mean_std[1] if fp_confidence_senior_unassisted_mean_std else 0]

    width = 0.4  # Adjust the width of the bars
    x = np.arange(len(labels))  # x positions for the bars

    fig, axs = plt.subplots(2, 2, figsize=(14, 6))  # 1 row, 2 columns

    # Plotting the bars closer together for Junior and Senior
    sns.set_style("white")  # Light green background
    axs[0, 0].set_facecolor('azure')
    axs[0, 0].bar(x - width, tp_assisted_means[0], width, yerr=tp_assisted_stds[0], capsize=5, label='Junior', color='royalblue', edgecolor='black')
    axs[0, 0].bar(x, tp_assisted_means[1], width, yerr=tp_assisted_stds[1], capsize=5, label='Senior', color='limegreen', edgecolor='black')
    axs[0, 0].set_title('True Positives (TP) - AI-assisted')
    axs[0, 0].set_xticks([])  # Remove x-ticks
    axs[0, 0].set_ylabel('Confidence (%)')
    # axs[0, 0].yaxis.grid(True)  # Adding horizontal grid lines
    axs[0, 0].set_yticks(np.arange(0, 110, 10))  # Setting y-ticks to be every 10 confidence points
    axs[0, 0].set_ylim(0, 110)
    # axs[0, 0].legend()  # Adding a legend to distinguish between Junior and Senior

    # Top right: FP AI-assisted
    sns.set_style("dark")  # Light red background
    axs[0, 1].set_facecolor('mistyrose')
    axs[0, 1].bar(x - width, fp_assisted_means[0], width, yerr=fp_assisted_stds[0], capsize=5, label='Junior', color='royalblue', edgecolor='black')
    axs[0, 1].bar(x, fp_assisted_means[1], width, yerr=fp_assisted_stds[1], capsize=5, label='Senior', color='limegreen', edgecolor='black')
    axs[0, 1].set_title('False Positives (FP) - AI-assisted')
    axs[0, 1].set_xticks([])  # Remove x-ticks
    axs[0, 1].set_ylabel('Confidence (%)')
    # axs[0, 1].yaxis.grid(True)  # Adding horizontal grid lines
    axs[0, 1].set_yticks(np.arange(0, 110, 10))  # Setting y-ticks to be every 10 confidence points
    axs[0, 1].set_ylim(0, 110)
    # axs[0, 1].legend()  # Adding a legend to distinguish between Junior and Senior

    # Bottom left: TP Unassisted
    sns.set_style("white")  # Light green background
    axs[1, 0].set_facecolor('azure')
    axs[1, 0].bar(x - width, tp_unassisted_means[0], width, yerr=tp_unassisted_stds[0], capsize=5, label='Junior', color='royalblue', edgecolor='black')
    axs[1, 0].bar(x, tp_unassisted_means[1], width, yerr=tp_unassisted_stds[1], capsize=5, label='Senior', color='limegreen', edgecolor='black')
    axs[1, 0].set_title('True Positives (TP) - Unassisted')
    axs[1, 0].set_xticks([])  # Remove x-ticks
    axs[1, 0].set_ylabel('Confidence (%)')
    # axs[1, 0].yaxis.grid(True)  # Adding horizontal grid lines
    axs[1, 0].set_yticks(np.arange(0, 110, 10))  # Setting y-ticks to be every 10 confidence points
    axs[1, 0].set_ylim(0, 110)
    # axs[1, 0].legend()  # Adding a legend to distinguish between Junior and Senior

    # Bottom right: FP Unassisted
    sns.set_style("dark")  # Light red background
    axs[1, 1].set_facecolor('mistyrose')
    axs[1, 1].bar(x - width, fp_unassisted_means[0], width, yerr=fp_unassisted_stds[0], capsize=5, label='Junior', color='royalblue', edgecolor='black')
    axs[1, 1].bar(x, fp_unassisted_means[1], width, yerr=fp_unassisted_stds[1], capsize=5, label='Senior', color='limegreen', edgecolor='black')
    axs[1, 1].set_title('False Positives (FP) - Unassisted')
    axs[1, 1].set_xticks([])  # Remove x-ticks
    axs[1, 1].set_ylabel('Confidence (%)')
    # axs[1, 1].yaxis.grid(True)  # Adding horizontal grid lines
    axs[1, 1].set_yticks(np.arange(0, 110, 10))  # Setting y-ticks to be every 10 confidence points
    axs[1, 1].set_ylim(0, 110)
    # axs[1, 1].legend()  # Adding a legend to distinguish between Junior and Senior

    plt.tight_layout()
    plt.show()


def main():
    # junior
    tp_confidence_junior_assisted_mean_std = [88, 2.5]
    tp_confidence_junior_unassisted_mean_std = [94, 1.9]
    fp_confidence_junior_assisted_mean_std = [45, 3.3]
    fp_confidence_junior_unassisted_mean_std = [42, 3.5]

    # senior
    tp_confidence_senior_assisted_mean_std = [94, 1.6]
    tp_confidence_senior_unassisted_mean_std = [94, 1.2]
    fp_confidence_senior_assisted_mean_std = [100, 0.]
    fp_confidence_senior_unassisted_mean_std = []

    plot_confidence_barplot(tp_confidence_junior_assisted_mean_std,
                            tp_confidence_junior_unassisted_mean_std,
                            fp_confidence_junior_assisted_mean_std,
                            fp_confidence_junior_unassisted_mean_std,
                            tp_confidence_senior_assisted_mean_std,
                            tp_confidence_senior_unassisted_mean_std,
                            fp_confidence_senior_assisted_mean_std,
                            fp_confidence_senior_unassisted_mean_std)


if __name__ == '__main__':
    main()
