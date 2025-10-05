def parse_message(message: str):
    result = {}
    try:
        tmp = message.strip().split("\n")
        
        record_count = int(tmp[0])
        records = [float(el.strip()) for el in tmp[1].split(',')]
        
        diff_count = int(tmp[2])
        
        # Исправляем парсинг пар (diff, erate)
        diffs_and_erate = []
        for i in range(3, 3 + diff_count):
            if i < len(tmp):
                parts = tmp[i].split(',')
                if len(parts) == 2:
                    diff = float(parts[0].strip())
                    erate = float(parts[1].strip())
                    diffs_and_erate.append((diff, erate))
        
        result = {
            "success": True,
            "record_count": record_count,
            "records": records,
            "diff_count": diff_count,
            "diffs_and_erate": diffs_and_erate,
        }

        return result 
    except Exception as e:
       return None
    