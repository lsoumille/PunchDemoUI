
class FileHelper:

    def saveToPIDFile(self, pids):
        f = open('.pid', 'w+')
        for pid in pids:
            if pid == '':
                continue
            f.write(pid + '\n')
        f.close()
        print("End to File Helper")
        return

    def getSavedPids(self):
        with open('.pid', 'r+') as f:
            pids = []
            for line in f:
                if line == '' or line == '\n':
                    continue
                pids.append(line)
            f.close()
            return pids

