class User:
  def __init__(self, id: int, name: str, username: str, password: str):
    self.__id = id
    self.__name = name
    self.__username = username
    self.__password = password

  def __eq__(self, __o):
    return self.__id == __o.__id and self.__name == __o.__name and self.__username == __o.__username and self.__password == __o.__password

  def getId(self):
    return self.__id
  
  def getName(self):
    return self.__name

  def getUsername(self):
    return self.__username

  def getPassword(self):
    return self.__password


  def setId(self, id: int):
    self.__id = id

  def setName(self, name: str):
    self.__name = name

  def setUsername(self, username: str):
    self.__username = username

  def setPassword(self, password: str):
    self.__password = password

class Admin:
  def __init__(self,  username: str, password: str):
    self.__username = username
    self.__password = password

  def __eq__(self, __o):
    return self.__username == __o.__username and self.__password == __o.__password

class Director(User):
  def __init__(self, id: int, name: str, username: str, password: str):
    super().__init__(id, name, username, password)
    self.__username = username

  def __eq__(self, __o):
    return self.__username == __o.__username

class CustomerService(User):
  def __init__(self, id: int, name: str, username: str, password: str):
    super().__init__(id, name, username, password)
    self.__username = username

  def __eq__(self, __o):
    return self.__username == __o.__username

class Teller(User):
  def __init__(self, id: int, name: str, username: str, password: str):
    super().__init__(id, name, username, password)
    self.__username = username

  def __eq__(self, __o):
    return self.__username == __o.__username

class Member:
  def __init__(self, id: int, name: str):
    self.__id = id
    self.__name = name

  def __eq__(self, __o):
    return self.__id ==__o.__id

  def getId(self):
    return self.__id

  def getName(self):
    return self.__name

  def setName(self, name: str):
    self.__name = name

class Transaction:
  def __init__(self, id: int, member: Member, amount: int, type: str):
    self.__id = id
    self.__member = member
    self.__amount = amount
    self.__type = type

  def getId(self):
    return self.__id

  def getMember(self):
    return self.__member

  def getAmount(self):
    return self.__amount

  def getType(self):
    return self.__type

class BankResource:
  __directors = []
  __tellers = []
  __customerServices = []
  __members = []
  __transactions = []

  def getDirectors(self):
    return self.__directors

  def getCustomerServices(self):
    return self.__customerServices
  
  def getTellers(self):
    return self.__tellers

  def getMembers(self):
    return self.__members

  def getTransactions(self):
    return self.__transactions
  
  def addDirector(self, director: Director):
    self.__directors.append(director)

  def addTeller(self, teller: Teller):
    self.__tellers.append(teller)

  def addCustomerService(self, cust: CustomerService):
    self.__customerServices.append(cust)

  def addMember(self, member: Member):
    self.__members.append(member)

  def addTransaction(self, transaction: Transaction):
    self.__transactions.append(transaction)

class Activity:
  def __init__(self, data: BankResource, parent):
    self.data = data
    self.parent = parent

  def index(self):
    pass

  def show(self):
    pass

  def add(self):
    pass

  def edit(self):
    pass

class DirectorActivity(Activity):
  def index(self):
    print('-------------')
    print('Data Direktur')
    print('-------------')
    print('1) List Direktur')
    print('2) Tambah Direktur')
    print('3) Edit Direktur')
    print('4) Kembali')
    pilihan = int(input('Pilihan anda: '))

    if pilihan == 1:
      self.show()

    elif pilihan == 2:
      self.add()

    elif pilihan == 3:
      self.edit()

    elif pilihan == 4:
      self.parent.adminIndex()

    else:
      print('Pilihan tidak ada!')
      self.index(self)
    return super().index()

  def show(self):
    for i in self.data.getDirectors():
      print('ID      : {}'.format(i.getId()))
      print('Nama    : {}'.format(i.getName()))
      print('Username: {}'.format(i.getUsername()))
      print('--------------------')
    self.index()
    return super().show()

  def add(self):
    id = len(self.data.getDirectors()) + 1
    name = input('Nama: ')
    username = input('Username: ')
    password = input('Password: ')

    new_director = Director(id, name, username, password)
    self.data.addDirector(new_director)

    print('Direktur berhasil ditambahkan!')
    self.index()
    return super().add()
    
  def edit(self):
    try:
      username = input('Username Direktur: ')
      match = Director(None, None, username, None)
      index = self.data.getDirectors().index(match)

      updated = self.data.getDirectors()[index]

      old_name = updated.getName()
      old_username = updated.getUsername()
      old_password = updated.getPassword()

      new_name = input('Nama (kosongkan jika tidak berubah): ')
      new_username = input('Username (kosongkan jika tidak berubah): ')
      new_password = input('Password (kosongkan jika tidak berubah): ')
      
      updated.setName(new_name) if len(new_name) > 0 else updated.setName(old_name)
      updated.setUsername(new_username) if len(new_username) > 0 else updated.setUsername(old_username)
      updated.setPassword(new_password) if len(new_password) > 0 else updated.setPassword(old_password)

      print('Direktur berhasil diupdate!')
      self.index()
      return super().edit()
    
    except Exception:
      print('Direktur tidak ditemukan!')
      self.index()

class TellerActivity(Activity):
  def index(self):
    print('-----------')
    print('Data Teller')
    print('-----------')
    print('1) List Teller')
    print('2) Tambah Teller')
    print('3) Edit Teller')
    print('4) Kembali')
    pilihan = int(input('Pilihan anda: '))

    if pilihan == 1:
      self.show()
      self.index()

    elif pilihan == 2:
      self.add()

    elif pilihan == 3:
      self.edit()

    elif pilihan == 4:
      self.parent.adminIndex()

    else:
      print('Pilihan tidak ada!')
      self.index()
    return super().index()

  def show(self):
    for i in self.data.getTellers():
      print('ID      : {}'.format(i.getId()))
      print('Nama    : {}'.format(i.getName()))
      print('Username: {}'.format(i.getUsername()))
      print('--------------------')
    return super().show()

  def add(self):
    id = len(self.data.getTellers()) + 1
    name = input('Nama: ')
    username = input('Username: ')
    password = input('Password: ')

    new_teller = Teller(id, name, username, password)
    self.data.addTeller(new_teller)
    
    print('Teller berhasil ditambahkan!')
    self.index()
    return super().add()

  def edit(self):
    try:
      username = input('Username Teller: ')
      match = Teller(None, None, username, None)
      index = self.data.getTellers().index(match)

      updated = self.data.getTellers()[index]

      old_name = updated.getName()
      old_username = updated.getUsername()
      old_password = updated.getPassword()

      new_name = input('Nama (kosongkan jika tidak berubah): ')
      new_username = input('Username (kosongkan jika tidak berubah): ')
      new_password = input('Password (kosongkan jika tidak berubah): ')
      
      updated.setName(new_name) if len(new_name) > 0 else updated.setName(old_name)
      updated.setUsername(new_username) if len(new_username) > 0 else updated.setUsername(old_username)
      updated.setPassword(new_password) if len(new_password) > 0 else updated.setPassword(old_password)

      print('Teller berhasil diupdate!')
      self.index()
    
    except Exception:
      print('Teller tidak ditemukan!')
      self.index()

    return super().edit()

class MemberActivity(Activity):
  def index(self):
    print('-----------')
    print('Data Member')
    print('-----------')
    print('1) List Member')
    print('2) Tambah Member')
    print('3) Edit Member')
    print('4) Kembali')
    pilihan = int(input('Pilihan anda: '))

    if pilihan == 1:
      self.show()
      self.index()

    elif pilihan == 2:
      self.add()

    elif pilihan == 3:
      self.edit()

    elif pilihan == 4:
      self.parent.customerServiceIndex()

    else:
      print('Pilihan tidak ada!')
      self.index()

    return super().index()

  def show(self):
    for i in self.data.getMembers():
      print('ID      : {}'.format(i.getId()))
      print('Nama    : {}'.format(i.getName()))
      print('--------------------')
    
    return super().show()

  def add(self):
    id = len(self.data.getMembers()) + 1
    name = input('Nama: ')

    new_member = Member(id, name)
    self.data.addMember(new_member)
    
    print('Member berhasil ditambahkan!')
    self.index()

    return super().add()

  def edit(self):
    try:
      id = int(input('ID Member: '))
      match = Member(id, None)
      index = self.data.getMembers().index(match)

      updated = self.data.getMembers()[index]

      old_name = updated.getName()

      new_name = input('Nama (kosongkan jika tidak berubah): ')
      
      updated.setName(new_name) if len(new_name) > 0 else updated.setName(old_name)

      print('Member berhasil diupdate!')
      self.index()
    
    except Exception:
      print('Member tidak ditemukan!')
      self.index()
    
    return super().edit()

class TransactionActivity(Activity):
  def index(self):
    print('--------------')
    print('Data Transaksi')
    print('--------------')
    print('1) List Transaksi')
    print('2) Tambah Transaksi')
    print('3) Kembali')
    pilihan = int(input('Pilihan anda: '))

    if pilihan == 1:
      self.show()
      self.index()

    elif pilihan == 2:
      self.add()

    elif pilihan == 3:
      self.parent.tellerSection()

    else:
      print('Pilihan tidak ada!')
      self.index()

    return super().index()

  def show(self):
    for i in self.data.getTransactions():
      member = i.getMember()
      print('ID      : {}'.format(i.getId()))
      print('Nasabah : {}'.format(member.getName()))
      print('Jumlah  : Rp{}'.format(i.getAmount()))
      print('Jenis   : {}'.format(i.getType()))
      print('--------------------')
    
    return super().show()

  def add(self):
    self.parent.member.show()
    member_id = int(input('ID Member: '))
    match = Member(member_id, None)
    index = self.data.getMembers().index(match)

    id = len(self.data.getTransactions()) + 1
    member = self.data.getMembers()[index]
    amount = int(input('Nominal: Rp'))
    type = input('Jenis Transaksi (debit/kredit/bunga/biaya administrasi): ')

    new_transaction = Transaction(id, member, amount, type)
    self.data.addTransaction(new_transaction)
    
    print('Transaksi berhasil ditambahkan!')
    self.index()

    return super().add()

class CustomerServiceActivity(Activity):
  def show(self):
    for i in self.data.getCustomerServices():
      print('ID      : {}'.format(i.getId()))
      print('Nama    : {}'.format(i.getName()))
      print('Username: {}'.format(i.getUsername()))
      print('--------------------')
    
    return super().show()

class MainActivity:
  data = BankResource()
  admin = Admin('admin', 'admin')

  direktur1 = Director(1, 'Head Director', 'dir1', 'dir1')
  direktur2 = Director(2, 'Vice Director', 'dir2', 'dir2')
  data.addDirector(direktur1)
  data.addDirector(direktur2)
  
  cs1 = CustomerService(1, 'Marketing Division', 'cs1', 'cs1')
  cs2 = CustomerService(2, 'Tech Support', 'cs2', 'cs2')
  data.addCustomerService(cs1)
  data.addCustomerService(cs2)

  teller1 = Teller(1, 'Teller 1', 'teller1', 'teller1')
  teller2 = Teller(2, 'Teller 2', 'teller2', 'teller2')
  data.addTeller(teller1)
  data.addTeller(teller2)

  member1 = Member(1, 'Marcus Horizon')
  member2 = Member(2, 'Sweet Home Alabama')
  data.addMember(member1)
  data.addMember(member2)

  transaction1 = Transaction(1, member1, 200000, 'debit')
  transaction2 = Transaction(2, member2, 750000, 'kredit')
  data.addTransaction(transaction1)
  data.addTransaction(transaction2)

  def __init__(self) -> None:
    self.teller = TellerActivity(self.data, self)
    self.member = MemberActivity(self.data, self)
    self.director = DirectorActivity(self.data, self)
    self.transaction = TransactionActivity(self.data, self)
    self.cs = CustomerServiceActivity(self.data, self)

  def index(self):
    print('-------------')
    print('Login sebagai')
    print('-------------')
    print('1) Admin')
    print('2) Direktur')
    print('3) Customer Service')
    print('4) Teller')
    print('5) Exit')

    pilihan = int(input('Pilihan anda: '))
    if pilihan == 1:
      self.adminSection()
    elif pilihan == 2:
      self.directorSection()
    elif pilihan == 3:
      self.customerServiceSection()
    elif pilihan == 4:
      self.tellerSection()
    elif pilihan == 5:
      print('Terima kasih!')
    else:
      print('Pilihan tidak ada!')

  def adminSection(self):
    print('--------------')
    print('Silahkan Login')
    print('--------------')
    username = input('Username: ')
    password = input('Password: ')
    
    login = Admin(username, password)
    if login == self.admin:
      self.adminIndex()

    else:
      print('Username atau password salah!')
      self.adminSection()

  def adminIndex(self):
    print('---------------')
    print('Welcome, Admin!')
    print('---------------')
    print('1) Data Direktur')
    print('2) Data Teller')
    print('3) Logout')
    pilihan = int(input('Pilihan anda: '))
    if pilihan == 1:
      self.director.index()
    elif pilihan == 2:
      self.teller.index()
    elif pilihan == 3:
      self.index()
    else:
      print('Pilihan tidak ada!')
      self.adminIndex()

  def directorSection(self):
    print('--------------')
    print('Silahkan Login')
    print('--------------')

    input_username = input('Username: ')
    input_password = input('Password: ')
    try:
      match = Director(None, None, input_username, None)
      index = self.data.getDirectors().index(match)

      director = self.data.getDirectors()[index]
      correct_password = director.getPassword()

      if input_password == correct_password:
        self.directorIndex()
      else:
        print('Username atau password salah!')
        self.directorSection()

    except Exception:
      print('Username atau password salah!')
      self.directorSection()

  def directorIndex(self):
    print('------------------')
    print('Welcome, Direktur!')
    print('------------------')
    print('1) Data Transaksi Keuangan Nasabah')
    print('2) Laporan Keuangan Bank')
    print('3) Data Customer Service')
    print('4) Data Teller')
    print('5) Logout')

    pilihan = int(input('Pilihan anda: '))
    if pilihan == 1:
      self.transaction.show()
      self.directorIndex()
    elif pilihan == 2:
      print('-----------------')
      print('Tidak ada laporan')
      print('-----------------')
      self.directorIndex()
    elif pilihan == 3:
      self.cs.show()
      self.directorIndex()
    elif pilihan == 4:
      self.teller.show()
      self.directorIndex()
    elif pilihan == 5:
      self.index()
    else:
      print('Pilihan tidak ada!')
      self.directorIndex()

  def customerServiceSection(self):
    print('--------------')
    print('Silahkan Login')
    print('--------------')

    input_username = input('Username: ')
    input_password = input('Password: ')
    try:
      match = CustomerService(None, None, input_username, None)
      index = self.data.getCustomerServices().index(match)

      cs = self.data.getCustomerServices()[index]
      correct_password = cs.getPassword()

      if input_password == correct_password:
        self.customerServiceIndex()
      else:
        print('Username atau password salah!')
        self.customerServiceSection()

    except Exception:
      print('Username atau password salah!')
      self.customerServiceSection()

  def customerServiceIndex(self):
    print('--------------------------')
    print('Welcome, Customer Service!')
    print('--------------------------')
    print('1) Data Nasabah')
    print('2) Logout')
    pilihan = int(input('Pilihan anda: '))

    if pilihan == 1:
      self.member.index()

    elif pilihan == 2:
      self.index()

    else:
      print('Pilihan tidak ada!')
      self.member.index()

  def tellerSection(self):
    print('--------------')
    print('Silahkan Login')
    print('--------------')

    input_username = input('Username: ')
    input_password = input('Password: ')
    try:
      match = Teller(None, None, input_username, None)
      index = self.data.getTellers().index(match)

      teller = self.data.getTellers()[index]
      correct_password = teller.getPassword()

      if input_password == correct_password:
        self.tellerIndex()
      else:
        print('Username atau password salah!')
        self.tellerSection()

    except Exception:
      print('Username atau password salah!')
      self.tellerSection()

  def tellerIndex(self):
    print('----------------')
    print('Welcome, Teller!')
    print('----------------')
    print('1) Transaksi Nasabah')
    print('2) Logout')
    pilihan = int(input('Pilihan anda: '))

    if pilihan == 1:
      self.transaction.index()

    elif pilihan == 2:
      self.index()

    else:
      print('Pilihan tidak ada!')
      self.tellerIndex()


main = MainActivity()
main.index()