meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
    "GOAT": "Greatest of all time",
    "CHUUYA": "Chuuya Nakahara",
            }

word = input("What word do you not understand:")

if word in meme_dict.keys():
    print(meme_dict[word])

else:
    print("Huhhh??")
