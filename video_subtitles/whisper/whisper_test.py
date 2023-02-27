import whisper

model = whisper.load_model("base")
result = model.transcribe("trump.mp3")
encoded_text = result["text"].encode("utf-8")
print(result["text"])

print("===============what is segments=================")
print(result["segments"])


# print(encoded_text)
# print(type(result))
# with open("result.txt", 'wb') as f:
	# f.write(encoded_text)