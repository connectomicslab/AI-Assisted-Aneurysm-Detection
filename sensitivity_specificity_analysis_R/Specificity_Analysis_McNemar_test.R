# McNemar test specificity analysis

print("Specificity analysis:")
print("")

cont_matrix_junior <-
  matrix(c(34, 11, 9, 9),
         nrow = 2,
         dimnames = list("unassisted_jun" = c("TN", "FP"),
                         "AI-assist_jun" = c("TN", "FP")))

cont_matrix_senior <-
  matrix(c(62, 1, 0, 0),
         nrow = 2,
         dimnames = list("unassisted_jun" = c("TN", "FP"),
                         "AI-assist_jun" = c("TN", "FP")))

result_junior <- mcnemar.test(cont_matrix_junior, correct = FALSE)
results_senior <- mcnemar.test(cont_matrix_senior, correct = FALSE)

# Print the performance matrix
print("Contringency Matrixes:")
print("    Junior")
print(cont_matrix_junior)
print("")
print("    Senior")
print(cont_matrix_senior)

print("McNemar Test Results:")
print("    Junior")
print(result_junior)
print("")
print("    Senior")
print(results_senior)