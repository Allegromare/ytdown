from pytube import YouTube

link = "https://www.youtube.com/watch?v=6pgodt1mezg"
src = YouTube(link)

# DOWNLOAD CAPTIONS

# prints all available captions in various languages.
print("Captions Available: ", src.captions)
print()

# Getting only English captions by specifying 'en' as parameter
en_caption = src.captions.get_by_language_code("en")
print(en_caption.xml_captions)

# Instead of Captions in XML format we are converting it to string format.
en_caption_convert_to_srt = en_caption.generate_srt_captions()
print(en_caption_convert_to_srt)
