#!/usr/bin/python3

if "/".join(__import__('sys').argv[0].split("\\")).split("/")[-1] != "dump_marshal.py":
    __import__('sys').exit(1)
try:
    if "/".join(__file__.split("\\")).split("/")[-1] != "dump_marshal.py":
        __import__('sys').exit(1)
except:
    pass


print(">>> Marshal dump by KhanhNguyen9872")
print(">>> FB: https://fb.me/khanh10a1")
print("!! ĐÂY LÀ TOOL SHARE FREE TẠI GITHUB KHANHNGUYEN9872 !!")
print("!! NẾU BẠN MUA TOOL NÀY TỪ MỘT AI ĐÓ, HỌ LÀ LỪA ĐẢO !!")
print()

__pypath__ = __import__('os').getcwd()

def rm_dir(dir):
    try:
        __import__("shutil").rmtree(dir)
    except:
        pass
rm_dir('__pycache__')

pyver = ".".join(__import__('sys').version.split(" ")[0].split(".")[:-1])
print(">> Python: {}".format(pyver))

while 1:
    try:
        file = input(">> Input file have marshal: ").replace("\"","")
        sieu_nhan_gao_xanh = open(file, 'rb').read(4)
        if b"\r\r\n" in sieu_nhan_gao_xanh:
            day_la_binary = True
        else:
            day_la_binary = False
        if int(__import__('os').stat(file).st_size) > 536870912:
            print('>> this file too large!')
            continue
        break
    except FileNotFoundError:
        print('>> file not found!')
    except PermissionError:
        print('>> permission denied!')
    except OSError:
        continue

data = open(file,'rb').read()

data_dump = ""

if day_la_binary:
    for i in range(1,31):
        try:
            if "<code object <module> at " in str(__import__('marshal').loads(data[i:])):
                data_dump = data[i:]
                break
        except:
            continue
else:
    data_dump = data
    data = ''

if not data_dump:
    print("!! file error !!")
    __import__('sys').exit()

__file__="{}".format(".".join("/".join(file.split("\\")).split("/")[-1].split(".")[:-1]))

list_rand = []
def random_str(length = 24):
    global list_rand
    while 1:
        rand = __import__('random').choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") + "".join([__import__('random').choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0987654321") for i in range(length)])
        if rand in list_rand:
            continue
        break
    list_rand.append(rand)
    return rand

open('khanhnguyen9872.py','w').write('exec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode('+str(__import__("base64").b64encode(__import__("zlib").compress(__import__('marshal').dumps(compile(r'''
try:
    if __name__=='__main__':
        try:__import__('os').unlink(__import__('sys').argv[0])
        except:pass
        try:__import__('os').unlink(__file__)
        except:pass
        try:__import__('os').unlink('khanhnguyen9872.py')
        except:pass
        __import__('sys').exit(1)
    from marshal import *
except:
    __import__('sys').exit(1)
else:pass
finally:import marshal
try:
    {5} = __import__('builtins').compile
    global {4}
    {4} = 0
    __file__ = """{3}"""
except:
    __import__('sys').exit(1)
else:pass
finally:pass
def loads(bytes):
    global {4}
    open('{{}}_dump/dump_{{}}_{{}}.txt'.format('{0}',{4},'{0}'),'w').write("# marshal dump by KhanhNguyen9872\n# file name: [{0}.py] ({1} - {2})\n# dump count -> " + str({4}) + "\n\nexec(__import__('marshal').loads(" + str(bytes) + "))\n")
    print('dump count -> {{}} completed (marshal)!'.format({4}))
    {4} += 1
    return marshal.loads(bytes)
def compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1):
    global {4}
    try:
        source=source.decode('utf8')
    except:
        pass
    open('{{}}_dump/dump_{{}}_{{}}_code.txt'.format('{0}',{4},'{0}'),'w').write("""# marshal dump by KhanhNguyen9872\n# file name: [{0}.py] ({1} - {2})\n# dump count -> """ + str({4}) + """\n# this is a code string!\n\n""" + str(source) + """\n""")
    print('dump count -> {{}} completed (code)!'.format({4}))
    {4} += 1
    return {5}(source, filename, mode, flags, dont_inherit, optimize)

'''.format(
        __file__,
        str('pyc' if day_la_binary else 'py'), 
        pyver,
        "{}".format("/".join(file.split("\\")).split("/")[-1]),
        random_str(),
        random_str(),
    ),'<KhanhNguyen9872>','exec'))))[::-1])+"[::-1]))),globals())")
try:
    __import__('os').chdir(__import__('os').path.dirname(file))
except:
    pass
rm_dir('__pycache__')
rm_dir(__file__ + "_dump")
try:
    __import__('os').mkdir(__file__ + "_dump")
except:
    pass
__file__="/".join(file.split("\\")).split("/")[-1]
__name__='__main__'
__import__('sys').argv[0]=__file__

marshal=br""

if data:
    marshal+=br'code=__import__("marshal").loads(' + str(data_dump).encode() + b')\n'

marshal+=r'''
try:
    __import__('khanhnguyen9872').__spec__ = __import__('marshal').__spec__
    __import__('sys').modules['marshal'] = __import__('sys').modules['khanhnguyen9872']
    __import__('marshal').loads.__name__ = 'loads'
    __import__('marshal').loads.__module__ = 'marshal'
    __import__('builtins').compile = __import__('khanhnguyen9872').compile
    __import__('builtins').compile.__name__ = 'compile'
    __import__('builtins').compile.__module__ = 'builtins'
    __builtins__ = __import__('builtins')
except:
    __import__('os').unlink(r'{}/khanhnguyen9872.py')
    __import__('sys').exit(1)
'''.format(__pypath__).encode('utf8')

if data:
    marshal+=br'exec(code,globals())'
else:
    marshal+=data_dump

marshal+="""\n\n__import__('os').unlink(r'{}/khanhnguyen9872.py')""".format(__pypath__).encode('utf8')

data = ""
data_dump
try:
    del list_rand, random_str,pyver, data, data_dump, day_la_binary, sieu_nhan_gao_xanh, file, rm_dir
except:
    pass
print("dumping....")
try:
    exec('import marshal;exec(marshal.loads(' + str(__import__('marshal').dumps(compile(marshal, '<KhanhNguyen9872>', 'exec'))) + "), globals())",globals())
except KeyboardInterrupt:
    pass
except Exception as e:
    __import__('logging').error(__import__('traceback').format_exc())
except:
    pass
try:
    __import__("shutil").rmtree(r'{}/__pycache__'.format(__pypath__))
except:
    pass
try:
    __import__('os').unlink(r'{}/khanhnguyen9872.py'.format(__pypath__))
except:
    pass
__import__('sys').exit()
