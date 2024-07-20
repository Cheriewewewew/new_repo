meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO": "untuk menjadi agrsif/marah"
            }
for i in range(5):
  word = input("\n Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
  
  if word in meme_dict.keys():
    print(meme_dict[word])
  else:
    print("kata tidak ditemukan")
  if word == "END":
    print("terimakasih telah menggunakan kamus ini!")
    break
