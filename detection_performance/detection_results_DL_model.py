import os
import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportion_confint
from utils_show_results import get_result_filename, detection_one_sub_for_conf_int, extract_unique_elements


__author__ = "Tommaso Di Noto"
__version__ = "0.0.1"
__email__ = "tommydino@hotmail.it"
__status__ = "Prototype"


def detection_all_sub_with_conf_int(prediction_dir: str,
                                    ground_truth_dir: str):
    subj_ses_count = 0  # initialize counter
    sens_list = []
    tp_list = []
    cnt_list = []
    fp_list = []
    all_subs = []
    for sub in sorted(os.listdir(os.path.join(prediction_dir))):  # loop over subjects
        if "sub" in sub and os.path.isdir(os.path.join(prediction_dir, sub)):
            for ses in sorted(os.listdir(os.path.join(prediction_dir, sub))):  # loop over sessions
                if "ses" in ses and os.path.isdir(os.path.join(prediction_dir, sub, ses)):
                    sub_int = int(sub[4:])
                    # only consider subs <= 717, != 646 and != 648 and != 657
                    if sub_int <= 717 and sub_int != 646 and sub_int != 648 and sub_int != 657:
                        all_subs.append(sub)
                        subj_ses_count += 1  # increment counter
                        print("\n{}) Subject {}_{}".format(subj_ses_count, sub, ses))

                        participant_dir = os.path.join(prediction_dir, sub, ses)
                        test_dir = os.path.join(ground_truth_dir, sub, ses)

                        # extract the result.txt file with the ground truth locations
                        result_filename = get_result_filename(participant_dir)

                        # extract the FROC parameters (FP, sensitivity, TP, cnt)
                        froc_params = detection_one_sub_for_conf_int(result_filename, test_dir)

                        fp_list.append(froc_params[0])  # append false positives

                        # if there are no NaNs
                        if not np.isnan(froc_params).any():
                            sens_list.append(froc_params[1])  # discard first element (not usable for the curve), extract sensitivity and append to external list
                            tp_list.append(froc_params[2])  # extract true positives and append to external list
                            cnt_list.append(froc_params[3])  # extract nb. aneurysms and append to external list

    all_subs_unique = extract_unique_elements(all_subs)  # only retain unique elements
    assert len(all_subs_unique) == 100, "There should be exactly 100 test subjects; found {} instead".format(len(all_subs_unique))

    sens_np = np.asarray(sens_list) * 100  # convert to %
    tps_df = pd.DataFrame(tp_list)
    cnts_df = pd.DataFrame(cnt_list)

    lower_bound = []
    upper_bound = []
    # loop over dataframe columns. Every column represents the nb. of allowed FP (e.g. first column 1 FP allowed, second column 2 FP allowed, ..)
    for column in tps_df:
        conf_int = proportion_confint(count=sum(tps_df[column]),
                                      nobs=sum(cnts_df[column]),
                                      alpha=0.05,
                                      method='wilson')  # compute 95% Wilson CI
        lower_bound.append(conf_int[0] * 100)
        upper_bound.append(conf_int[1] * 100)

    print("\n\n------------------------------------------------")
    print("\nMean sensitivity (95% Wilson CI): {}% ({}%, {}%)".format(np.mean(sens_np), lower_bound[0], upper_bound[0]))
    print("\nFP count = {}; average = {:.2f}".format(int(np.sum(fp_list)), np.mean(fp_list)))
    print("Total number of true positives: {}".format(np.sum(tp_list)))


def main():
    # extract paths needed to run this script
    prediction_dir = r"D:\Aneurysm_Project_Tommaso\Backup_data_dir_lausanne_aneurysms_HPC\final_inference_clinical_paper_TL_finetuning_thrsh_0_2_overlap_0_75_max_4_FP_reduce_FP_with_volume_chuv_all_random_neg_patches_src_adam_trg_chuv_from_600_to_732_Jan_17_2023\only_inference_Jan_17_2023"
    ground_truth_dir = r"D:\Aneurysm_Project_Tommaso\Backup_Aneurysm_Data_Feb_02_2023_first\Clinical_paper_May_2022\Ground_Truth_Test_Set_Clinical_Paper_100_subs_Feb_04_2024"

    # compute detection performance as performed in the ADAM challenge
    detection_all_sub_with_conf_int(prediction_dir,
                                    ground_truth_dir)


if __name__ == "__main__":
    main()
