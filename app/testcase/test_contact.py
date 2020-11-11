from app.page.app import APP


class TestContact:
    def setup(self):
        self.app=APP()
        self.main=self.app.start().goto_main()

    def test_addcontact(self):
        send_name='2124333912'
        send_mobile='15158667511'
        send_gender='女'
        result =self.main.goto_adress().\
            click_addmember().\
            add_member_menual().\
            add_contact(send_name,send_mobile,send_gender)


