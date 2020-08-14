def select_from(target, origin):
    return """SELECT (%s) FROM (%s)""" % (target, origin)


def select_count_from(target, origin, group):
    return """SELECT (%s), COUNT(*) FROM (%s) GROUP BY (%s)""" % (target, origin, group)


def select_avg_from_group_by_2(target, origin, const, var, group1, group2):
    return """SELECT AVG((%s)) FROM (%s) WHERE (%s)=(%s) GROUP BY (%s), (%s)""" % (target, origin, const, var, group1, group2)


def select_two_count_from(target, target1, origin, group, group1):
    return """SELECT (%s),(%s), COUNT(*) FROM (%s) GROUP BY (%s), (%s)""" % (target, target1, origin, group, group1)


def select_from_where_string(target, origin, const, var):
    return """SELECT (%s) FROM (%s) WHERE   (%s)=("%s") """ % (target, origin, const, var)


def select_all_from_where_string_and(origin, const1, var1, const2, var2):
    return """SELECT * FROM (%s) WHERE   (%s)=(%s)  AND (%s)=('%s')  """ % (origin, const1, var1, const2, var2)


def select_2_distinct_from(target, target1, origin):
    return """SELECT DISTINCT (%s), (%s) FROM (%s)""" % (target, target1, origin)
   

def select_tailnum(var):
    return"""SELECT COUNT(flights.tailnum) FROM flights INNER JOIN planes ON
            flights.tailnum = planes.tailnum WHERE planes.manufacturer
            = ('%s') """ %(var)


    