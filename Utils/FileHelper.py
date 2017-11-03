
class FileHelper:

    def saveToPIDFile(pids):
        f = open('.pid', 'w+')
        for pid in pids:
            if pid == '':
                continue
            f.write(pid + '\n')
        f.close()

    def getSavedPids(self):
        with open('.pid', 'r+') as f:
            pids = []
            for line in f:
                if line == '\n':
                    continue
                pids.append(line)
            return pids
