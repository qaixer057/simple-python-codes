import whisper
import json
model = whisper.load_model("base")
result = model.transcribe("trump.mp3")
encoded_text = result["text"].encode("utf-8")
# print(result["text"])

# print("===============what is segments=================")
# print(result["segments"])

print(result)
# print(encoded_text)
# print(type(result))
with open("result.txt", 'w') as f:
	f.write(json.dumps(result))