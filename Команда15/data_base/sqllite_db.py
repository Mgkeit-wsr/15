import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('hakaton.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS job(name TEXT, description TEXT, experience INT, salary INT)')
    base.commit()
    
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO job VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()