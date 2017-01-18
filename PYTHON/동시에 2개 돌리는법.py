import concurrent.futures as cf

with cf.ThreadPoolExecutor() as ex:
     ex.submit(function_a)
     ex.submit(function_b)
