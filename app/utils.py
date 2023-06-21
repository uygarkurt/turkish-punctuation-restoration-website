from transformers import pipeline

path = "uygarkurt/bert-restore-punctuation-turkish-V0"
auth_token = "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"

pipe = pipeline(task="token-classification", model=path, tokenizer=path, use_auth_token=auth_token)
mapping = {
	"PERIOD": ".",
	"COMMA": ",",
	"QUESTION_MARK": "?"}

def punctuation_restoration(inp):
	res = pipe(inp)
	for idx, ent in enumerate(res):
		inp = inp[:ent["start"]+idx] + ent["word"]+mapping[ent["entity"]] + inp[ent["end"]+idx:]
	return(inp)
