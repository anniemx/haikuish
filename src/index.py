import process_data

corpus = ("""Lorem ipsum dolor sit amet, 
          consectetur adipiscing elit. Nullam 
          nec lobortis nulla. Curabitur congue 
          interdum eros commodo suscipit. Phasellus 
          feugiat aliquam molestie. Nam est urna, pharetra 
          viverra auctor et, pellentesque quis ligula. 
          Morbi in consectetur ligula. Mauris eros est, 
          egestas ut vehicula vitae, volutpat at mi. Aliquam 
          posuere volutpat turpis.""")


process_data.generate_ngrams(corpus)