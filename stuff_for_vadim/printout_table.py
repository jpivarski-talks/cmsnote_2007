# In Python, nesting is represented by indentation.  What is
# considered in the loop and what is out of the loop is determined by
# how many spaces you include at the beginning of the line.

# The print statement puts carriage returns at the ends of lines by
# default.  To suppress this, add an extra comma (,) at the end of the
# line.  Commas also add a space.  To get more control over the
# output, see the printf()-like example after the for loops.

# load the geometry
execfile("muonGeometry.py")

# print out disks and wheels
for rawid, diskobject in disks.items():
    if diskobject.barrel:
        print "Not a disk but a wheel.  Wheel number =", diskobject.wheel, "and rawid =", rawid
    else:
        print "Disk number ", diskobject.disk, "and rawid =", rawid

# print out chambers
for rawid, chamberobject in chambers.items():
    if chamberobject.barrel:
        print "barrel DT chamber wheel =", chamberobject.wheel, " station =", chamberobject.station, " sector =", chamberobject.sector, "rawid =", rawid
    else:
        print "endcap CSC chamber disk =", chamberobject.disk, " ring =", chamberobject.ring, " chamber-in-disk =", chamberobject.chamber, "rawid =", rawid

# print out layers/superlayers
for rawid, layerobject in layers.items():
    if layerobject.barrel:
        print "Not a layer but a DT superlayer.  ", layerobject.wheel, layerobject.station, layerobject.sector, "superlayer# =", layerobject.superlayer, "rawid =", rawid
    else:
        print "Endcap CSC layer.  ", layerobject.disk, layerobject.ring, layerobject.chamber, "layer# =", layerobject.layer, "rawid =", rawid

print "No way to map DT layers to rawids.  Sorry--- we'll figure this out some other time."

# more stuff; you might find it useful, depending on how you want to structure your table.
print "Useful tricks--- this works like printf():"
print "string: %s, number: %d, number: %d, number: %d, floating-point: %g" % ("hello", 1, 2, 3, 4.1)

# a big sorting example
print "Sort chambers before printing:"

def sortfunction(a, b):
    # a.barrel and b.barrel are both boolean variables
    if a.barrel != b.barrel:
        return cmp(b.barrel, a.barrel)  # this puts the barrel first, endcap second
                                        # cmp() returns -1 or 1, depending on the order

    if a.barrel:

        if a.wheel != b.wheel:
            return cmp(a.wheel, b.wheel)
        if a.station != b.station:
            return cmp(a.station, b.station)
        if a.sector != b.sector:
            return cmp(a.sector, b.sector)
        return 0                        # 0 means that they're exactly the same

    else:

        if a.disk != b.disk:
            return cmp(a.disk, b.disk)
        if a.ring != b.ring:
            return cmp(a.ring, b.ring)
        if a.chamber != b.chamber:
            return cmp(a.chamber, b.chamber)
        return 0

sortable_chambers = chambers.values()
sortable_chambers.sort(sortfunction)
for chamberobject in sortable_chambers:
    print "rawid, everythingatonce =", chamberobject.rawid, chamberobject
