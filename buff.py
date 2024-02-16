"""
                        SELECT kari_club.field1, kari_club.field2, kari_club.field3, kari_club.field4, kari_club.field5, kari_club.field6, kari_club.field7, kari_club.field8, kari_club.field9, kari_club.field10, kari_club.field11, kari_club.field12, kari_club.field13
                        FROM kari_club 
                        WHERE kari_club.field1 LIKE :searchText OR kari_club.field2 LIKE :searchText OR kari_club.field3 LIKE:searchText OR kari_club.field4 LIKE:searchText OR kari_club.field5 LIKE:searchText OR kari_club.field6 LIKE:searchText OR kari_club.field7 LIKE:searchText OR kari_club.field8 LIKE:searchText OR kari_club.field9 LIKE:searchText OR kari_club.field10 LIKE:searchText OR kari_club.field11 LIKE:searchText OR kari_club.field12 LIKE:searchText OR kari_club.field13 LIKE:searchText
                        UNION
                        SELECT EYEOFGOD909.field1, EYEOFGOD909.field2, EYEOFGOD909.field3, EYEOFGOD909.field4, EYEOFGOD909.field5 
                        FROM EYEOFGOD909 
                        WHERE EYEOFGOD909.field1 LIKE :searchText OR EYEOFGOD909.field2 LIKE :searchText OR EYEOFGOD909.field3 LIKE:searchText OR EYEOFGOD909.field4 LIKE:searchText OR EYEOFGOD909.field5 LIKE:searchText
        """