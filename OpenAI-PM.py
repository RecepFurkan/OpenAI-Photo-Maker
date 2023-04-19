import openai

# OpenAI API anahtarını oku veya iste
try:
    with open("openai api key.txt" , "r") as f:
        api_key = f.read().strip()
        if not api_key:
            raise ValueError
except (FileNotFoundError, ValueError):
    api_key = input('OpenAI API anahtarını giriniz: ')
    with open("openai api key.txt" , "w") as f:
        f.write(api_key)

openai.api_key = api_key

# Görüntü oluşturmak için kullanılan metin al
prompt = input("Görüntü oluşturmak için kullanılacak metni girin: ")

# Resim boyutu iste ve seçeneği doğrula
print("Resim boyutu seçin: 1. 256x256, 2. 512x512, 3. 1024x1024")
size_option = input("Seçenek numarasını girin: ")
if size_option not in ["1", "2", "3"]:
    print("Hatalı girdi! Lütfen 1, 2 veya 3 seçeneklerinden birini girin.")
else:
    if size_option == "1":
        size = "256x256"
    elif size_option == "2":
        size = "512x512"
    else:
        size = "1024x1024"

    # Resim oluştur
    try:
        response = openai.Image.create(
            prompt=prompt,
            model="image-alpha-001",
            size=size,
            response_format="url"
        )
        print("Görüntü URL'si: ", response["data"][0]["url"])
    except Exception as e:
        print("Bir hata oluştu:", e)