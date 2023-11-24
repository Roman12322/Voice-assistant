# from audio import get_text_from_audiofile
# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer
#
#
# def get_extention_text(user_message):
#     # model config
#     tokenizer = AutoTokenizer.from_pretrained(
#         "stabilityai/StableBeluga-7B", use_fast=True
#     )
#     model = AutoModelForCausalLM.from_pretrained(
#         "stabilityai/StableBeluga-7B",
#         torch_dtype=torch.float16,
#         low_cpu_mem_usage=True,
#         device_map="auto",
#     )
#
#     # creating prompt that we pass to our model
#     system_prompt = "### System:\nYou are StableBeluga, an AI that follows instructions extremely well. \
#    Help as much as you can. Remember, be safe, and don't do anything illegal. \n\n"
#     message = f"{user_message}.  Сделай краткий отчет и пиши строго на русском языке. Создай глоссарий для предоставленного текста, включающий определения ключевых терминов, концепций и фраз, упомянутых в тексте. Обеспечь точные и краткие определения для каждого элемента, обозначая контекст их использования в тексте. Уделяй внимание специфике предметной области текста и включай соответствующие ссылки на источники или теории, если это необходимо."
#     prompt = f"{system_prompt}### User: {message}\n\n### Assistant:\n"
#
#     # get tokenized text
#     inputs = tokenizer(prompt, return_tensors="pt")
#     inputs = inputs.to("cuda")
#
#     # generate summarization of our text & hopefully get some terms
#     output = model.generate(
#         **inputs, do_sample=True, top_p=0.95, top_k=0, max_new_tokens=512
#     )
#
#     # upload it in json format
#     json_output = {
#         "user_message": user_message,
#         "answer": (tokenizer.decode(output[0], skip_special_tokens=True)),
#     }
#     return json_output
#
#
# #  path = 'C:\HackMSK\ML-model-MSK-Hackaton\\rec1.wav'
# #  user_message = get_text_from_audiofile(path=path)
# #  print(get_extention_text(user_message=user_message))
