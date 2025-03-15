import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon
import numpy as np

__author__ = "Tommaso Di Noto"
__version__ = "0.0.1"
__email__ = "tommydino@hotmail.it"
__status__ = "Prototype"


def plot_two_distributions_with_boxplots_and_beeswarm(distribution_1: pd.Series,
                                                      distribution_2: pd.Series,
                                                      label_dist_1: str,
                                                      label_dist_2: str,
                                                      plot_title: str):
    # create figure
    plt.figure()

    # convert to numpy array
    dist1_np = distribution_1.to_numpy()
    dist2_np = distribution_2.to_numpy()

    # Draw the bee-swarm plots of the two distributions with the overlayed boxplots
    sns.boxplot(data=[dist1_np, dist2_np], showfliers=False)
    sns.swarmplot(data=[dist1_np, dist2_np], color=".25")

    # Set the labels
    plt.xticks([0, 1], [label_dist_1, label_dist_2], fontsize=12)
    # Set y-axis label
    plt.ylabel("Seconds (s)", fontsize=12)
    # Set limits to the y-axis
    plt.ylim(25, 250)
    # Set the title
    plt.title(plot_title, fontsize=16, fontweight='bold')


# function to convert a string time format to seconds
def str_to_seconds(time_str: str) -> int:
    """This function converts a string time format to seconds
    Args:
        time_str: time in the format "m:ss"
    Returns:
        time_in_seconds: time in seconds
    """
    minutes, seconds = time_str.split('m')
    seconds = seconds.rstrip('s')

    time_in_seconds = int(minutes) * 60 + int(seconds)

    return time_in_seconds


def extract_reading_time_and_setting(df):
    # only keep the columns of interest
    columns_of_interest = ["sub", "reading_time", "read_setting"]
    df = df[columns_of_interest]

    # convert the format xmxxs to seconds for the column reading_time
    df["reading_time"] = df["reading_time"].apply(str_to_seconds)

    return df


def compare_timing_between_readings(path_first_read_junior_excel,
                                    path_second_read_junior_excel,
                                    path_first_read_senior_excel,
                                    path_second_read_senior_excel):
    """This function compares the reading times between two readings distributions
    Args:
        path_first_read_junior_excel (str): path to the Excel file with the first reading times of the junior
        path_second_read_junior_excel (str): path to the Excel file with the second reading times of the junior
        path_first_read_senior_excel (str): path to the Excel file with the first reading times of the senior
        path_second_read_senior_excel (str): path to the Excel file with the second reading times of the senior
    """
    # read Excel files with pandas
    df_first_read_junior = pd.read_excel(path_first_read_junior_excel)
    df_second_read_junior = pd.read_excel(path_second_read_junior_excel)
    df_first_read_senior = pd.read_excel(path_first_read_senior_excel)
    df_second_read_senior = pd.read_excel(path_second_read_senior_excel)

    # preprocess the dataframes
    df_first_read_junior = extract_reading_time_and_setting(df_first_read_junior)
    df_second_read_junior = extract_reading_time_and_setting(df_second_read_junior)
    df_first_read_senior = extract_reading_time_and_setting(df_first_read_senior)
    df_second_read_senior = extract_reading_time_and_setting(df_second_read_senior)

    # separate the dataframes by read setting for junior radiologist
    df_first_read_junior_assisted = df_first_read_junior[df_first_read_junior["read_setting"] == "assisted"]
    df_first_read_junior_unassisted = df_first_read_junior[df_first_read_junior["read_setting"] == "unassisted"]
    df_second_read_junior_assisted = df_second_read_junior[df_second_read_junior["read_setting"] == "assisted"]
    df_second_read_junior_unassisted = df_second_read_junior[df_second_read_junior["read_setting"] == "unassisted"]

    # separate the dataframes by read setting also for the senior
    df_first_read_senior_assisted = df_first_read_senior[df_first_read_senior["read_setting"] == "assisted"]
    df_first_read_senior_unassisted = df_first_read_senior[df_first_read_senior["read_setting"] == "unassisted"]
    df_second_read_senior_assisted = df_second_read_senior[df_second_read_senior["read_setting"] == "assisted"]
    df_second_read_senior_unassisted = df_second_read_senior[df_second_read_senior["read_setting"] == "unassisted"]

    # combine assisted and unassisted across the two readings for the junior
    all_assisted_junior = pd.concat([df_first_read_junior_assisted, df_second_read_junior_assisted])
    all_unassisted_junior = pd.concat([df_first_read_junior_unassisted, df_second_read_junior_unassisted])

    # combine assisted and unassisted across the two readings for the senior
    all_assisted_senior = pd.concat([df_first_read_senior_assisted, df_second_read_senior_assisted])
    all_unassisted_senior = pd.concat([df_first_read_senior_unassisted, df_second_read_senior_unassisted])

    # sort by "sub": for the Wilcoxon signed-rank test we to compare subjects with the same order across the two readings
    # -- junior
    all_assisted_junior_sorted = all_assisted_junior.sort_values(by=["sub"])
    all_unassisted_junior_sorted = all_unassisted_junior.sort_values(by=["sub"])
    # -- senior
    all_assisted_senior_sorted = all_assisted_senior.sort_values(by=["sub"])
    all_unassisted_senior_sorted = all_unassisted_senior.sort_values(by=["sub"])

    # plot the 4 different scenarios
    # 1) ------------------------------- Reading time: Junior Assisted vs. Junior Unassisted -------------------------------
    plot_two_distributions_with_boxplots_and_beeswarm(distribution_1=all_assisted_junior_sorted["reading_time"],
                                                      distribution_2=all_unassisted_junior_sorted["reading_time"],
                                                      label_dist_1="AI-Assisted",
                                                      label_dist_2="Unassisted",
                                                      plot_title="Reading times: Junior")

    # 2) ------------------------------- Reading time: Senior Assisted vs. Senior Unassisted -------------------------------
    plot_two_distributions_with_boxplots_and_beeswarm(distribution_1=all_assisted_senior_sorted["reading_time"],
                                                      distribution_2=all_unassisted_senior_sorted["reading_time"],
                                                      label_dist_1="AI-Assisted",
                                                      label_dist_2="Unassisted",
                                                      plot_title="Reading times: Senior")

    # -------------------- Wilcoxon signed-rank test --------------------
    # ----- junior (assisted vs. unassisted)
    times_assisted_junior_sorted_np = all_assisted_junior_sorted["reading_time"].to_numpy()
    times_unassisted_junior_sorted_np = all_unassisted_junior_sorted["reading_time"].to_numpy()
    res_junior = wilcoxon(times_assisted_junior_sorted_np,
                          times_unassisted_junior_sorted_np,
                          zero_method="wilcox",  # discard zero differences
                          alternative="two-sided")  # two-sided: the alternative hypothesis is that the absolute difference between median is not equal to zero
    print(f"\nJunior: p-value: {res_junior.pvalue}, statistic: {res_junior.statistic}")
    print(f"    Median assisted: {np.median(times_assisted_junior_sorted_np)}")
    print(f"    Median unassisted: {np.median(times_unassisted_junior_sorted_np)}")

    # ----- senior (assisted vs. unassisted)
    times_assisted_senior_sorted_np = all_assisted_senior_sorted["reading_time"].to_numpy()
    times_unassisted_senior_sorted_np = all_unassisted_senior_sorted["reading_time"].to_numpy()
    res_senior = wilcoxon(times_assisted_senior_sorted_np,
                          times_unassisted_senior_sorted_np,
                          zero_method="wilcox",  # discard zero differences
                          alternative="two-sided")  # two-sided: the alternative hypothesis is that the absolute difference between median is not equal to zero
    print(f"\nSenior: p-value: {res_senior.pvalue}, statistic: {res_senior.statistic}")
    print(f"    Median assisted: {np.median(times_assisted_senior_sorted_np)}")
    print(f"    Median unassisted: {np.median(times_unassisted_senior_sorted_np)}")

    # ------------- junior vs. senior
    # assisted
    res_junior_vs_senior_assisted = wilcoxon(times_assisted_junior_sorted_np,
                                             times_assisted_senior_sorted_np,
                                             zero_method="wilcox",  # discard zero differences
                                             alternative="two-sided")  # two-sided: the alternative hypothesis is that the absolute difference between median is not equal to zero
    print(f"\nJunior vs. Senior (assisted): p-value: {res_junior_vs_senior_assisted.pvalue}, statistic: {res_junior_vs_senior_assisted.statistic}")

    # unassisted
    res_junior_vs_senior_unassisted = wilcoxon(times_unassisted_junior_sorted_np,
                                               times_unassisted_senior_sorted_np,
                                               zero_method="wilcox",  # discard zero differences
                                               alternative="two-sided")  # two-sided: the alternative hypothesis is that the absolute difference between median is not equal to zero
    print(f"\nJunior vs. Senior (unassisted): p-value: {res_junior_vs_senior_unassisted.pvalue}, statistic: {res_junior_vs_senior_unassisted.statistic}")

    # 3) ------------------------------- Reading time: Junior Assisted vs. Senior Assisted -------------------------------
    # plot_two_distributions_with_boxplots_and_beeswarm(distribution_1=all_assisted_junior["reading_time"],
    #                                                   distribution_2=all_assisted_senior["reading_time"],
    #                                                   label_dist_1="Junior",
    #                                                   label_dist_2="Senior",
    #                                                   plot_title="Reading times: Assisted")

    # 4) ------------------------------- Reading time: Junior Unassisted vs. Senior Unassisted -------------------------------
    # plot_two_distributions_with_boxplots_and_beeswarm(distribution_1=all_unassisted_junior["reading_time"],
    #                                                   distribution_2=all_unassisted_senior["reading_time"],
    #                                                   label_dist_1="Junior",
    #                                                   label_dist_2="Senior",
    #                                                   plot_title="Reading times: Unassisted")

    # show the plots
    plt.show()


def main():
    # input args
    path_first_read_junior_excel = r"path\to\READINGS\first_read\First_Read_Sofyan_Aneurysm_Clinical_Paper_Jan_19_2023.xlsx"
    path_second_read_junior_excel = r"path\to\READINGS\second_read\Second_Read_Sofyan_Aneurysm_Clinical_Paper_Jan_19_2023.xlsx"
    path_first_read_senior_excel = r"path\to\READINGS\first_read\First_Read_Francesco_Aneurysm_Clinical_Paper_Jan_19_2023.xlsx"
    path_second_read_senior_excel = r"path\to\READINGS\second_read\Second_Read_Francesco_Aneurysm_Clinical_Paper_Jan_19_2023.xlsx"

    compare_timing_between_readings(path_first_read_junior_excel,
                                    path_second_read_junior_excel,
                                    path_first_read_senior_excel,
                                    path_second_read_senior_excel)


if __name__ == '__main__':
    main()
