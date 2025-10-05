def parse_message(message: str):
     result = {}
     try:
          tmp = message.split("\n")

          record_count = int(tmp[0])
          records = [float(el) for el in tmp[1].split(', ')]

        
          result = {
                "record_count":record_count,
                "records": records,
                "i_erate": None,
          }
          if len(tmp) == 3:
               result["i_erate"] = float(tmp[2])
          return result
     except: 
         return None
