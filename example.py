from multichoicelib import MultiChoice

query = MultiChoice("Pick one:", ["apples", "cherries"]).wAccentColor("\033[33m").wQuestionPrefix("\033[4m").wAnswerPrefix("] ", True).wSelectedPrefix(") ", True).addOption("oranges")()

print(query.index, query.value)