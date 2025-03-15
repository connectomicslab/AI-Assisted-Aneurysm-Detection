# McNemar test sensitivity analysis

print("Sensitivity analysis:")
print("")

cont_matrix_junior <-
  matrix(c(31, 6, 8, 2),
         nrow = 2,
         dimnames = list("unassisted_jun" = c("TP", "FN"),
                         "AI-assist_jun" = c("TP", "FN")))

cont_matrix_senior <-
  matrix(c(37, 4, 4, 2),
         nrow = 2,
         dimnames = list("unassisted_jun" = c("TP", "FN"),
                         "AI-assist_jun" = c("TP", "FN")))

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


