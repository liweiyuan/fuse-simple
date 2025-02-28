from fuse import FUSE, FuseOSError, Operations, LoggingMixIn
import errno
import os

class SimpleFS(LoggingMixIn, Operations):
    def __init__(self):
        self.files = {
            '/': {'type': 'dir', 'st_mode': 0o40755},
            '/hello.txt': {
                'type': 'file',
                'st_mode': 0o100644,
                'content': b'Hello from FUSE!\n',
                'st_size': 16,
            },
            '/mydir': {'type': 'dir', 'st_mode': 0o40755},
        }

    # 获取文件/目录属性
    def getattr(self, path, fh=None):
        if path not in self.files:
            raise FuseOSError(errno.ENOENT)
        return self.files[path]

    # 读取目录内容
    def readdir(self, path, fh):
        entries = ['.', '..']
        for p in self.files:
            if p.startswith(path) and p != path:
                name = p[len(path):].lstrip('/')
                if '/' not in name:
                    entries.append(name)
        return entries

    # 打开文件
    def open(self, path, flags):
        if path not in self.files or self.files[path]['type'] != 'file':
            raise FuseOSError(errno.ENOENT)
        return 0  # 返回文件句柄（此处简化）

    # 读取文件内容
    def read(self, path, size, offset, fh):
        if path not in self.files:
            raise FuseOSError(errno.ENOENT)
        content = self.files[path]['content']
        return content[offset:offset + size]

if __name__ == '__main__':
    # 挂载到目录 ./myfs
    FUSE(SimpleFS(), './myfs', foreground=True, nothreads=True)