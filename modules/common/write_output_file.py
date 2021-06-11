def write_output_file(output_path, input_txt):
    f = open(output_path, 'w')
    f.write(input_txt)
    f.close()
