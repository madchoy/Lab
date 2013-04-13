import sys, os

#tests_dir = os.path.dirname( os.path.abspath(__file__) )
#src_dir = os.path.join(os.path.dirname(tests_dir),'src')



tests_dir = os.path.dirname( os.path.abspath(__file__) )
src_dir = os.path.join(os.path.dirname(tests_dir),'src')
#sys.path.insert(0, tests_dir)
#sys.path.append(src_dir)
sys.path.insert(0, src_dir)

def test_imports():
    print sys.path
    import pub_sub
