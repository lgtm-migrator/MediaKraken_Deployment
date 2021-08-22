"""
Example nzb file

<?xml version="1.0" encoding="iso-8859-1" ?>
<!DOCTYPE nzb PUBLIC "-//newzBin//DTD NZB 1.1//EN" "http://www.newzbin.com/DTD/nzb/nzb-1.1.dtd">
<nzb xmlns="http://www.newzbin.com/DTD/2003/nzb">
 <head>
   <meta type="title">Your File!</meta>
   <meta type="tag">Example</meta>
 </head>
 <file poster="Joe Bloggs <bloggs@nowhere.example>;" date="1071674882" subject="Here's your file!  abc-mr2a.r01 (1/2)">
   <groups>
     <group>alt.binaries.newzbin</group>
     <group>alt.binaries.mojo</group>
   </groups>
   <segments>
     <segment bytes="102394" number="1">123456789abcdef@news.newzbin.com</segment>
     <segment bytes="4501" number="2">987654321fedbca@news.newzbin.com</segment>
   </segments>
 </file>
</nzb>
"""
import xmltodict


def com_nzb_parse_to_dict(file_name):
    return xmltodict.parse(file_name)
