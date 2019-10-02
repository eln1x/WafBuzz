def printtable(rows):
  if len(rows) > 1:
    headers = rows[0]._fields
    lens = []
    for i in range(len(rows[0])):
      lens.append(len(max([x[i] for x in rows] + [headers[i]],key=lambda x:len(str(x)))))
    formats = []
    hformats = []
    for i in range(len(rows[0])):
      if isinstance(rows[0][i], int):
        formats.append("%%%dd" % lens[i])
      else:
        formats.append("%%-%ds" % lens[i])
      hformats.append("%%-%ds" % lens[i])
    pattern = " | ".join(formats)
    hpattern = " | ".join(hformats)
    separator = "-+-".join(['-' * n for n in lens])
    xtable = hpattern % tuple(headers)
    xtable += "\r\n"
    xtable += separator
    xtable += "\r\n"
    _u = lambda t: t.decode('UTF-8', 'replace') if isinstance(t, str) else t
    for line in rows:
        xtable  += pattern % tuple(_u(t) for t in line)
        xtable += "\r\n" 
        



  elif len(rows) == 1:
    row = rows[0]
    hwidth = len(max(row._fields,key=lambda x: len(x)))
    for i in range(len(row)):
      xtable += "%*s = %s" % (hwidth,row._fields[i],row[i])
      xtable += "\r\n"
  return xtable
