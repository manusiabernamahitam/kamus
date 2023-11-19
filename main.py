meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "AFK": "menjauh dari keyboard",
            "BRB": "pergi sebentar",
            }
            
while True:
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
                
    if word in meme_dict.keys():
        print("makna dari kata",word,meme_dict[word])
        
        
        
        
    else:
        print("kata tidak ditemukan!")
    
    question = input("apakah ingin lanjut? y atau n")
    
    if question == 'N':
        break
    
    else:
        continue
