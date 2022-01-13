import sqlite3
import aiosqlite

class DbFunc():
    def __init__(self, name="db.sqlite3"):
        self.name = name
        self.con = self.connect()

    async def connect(self):
        async with aiosqlite.connect(self.name) as db:
            await db.execute("INSERT INTO some_table ...")
            await db.commit()

            async with db.execute("SELECT * FROM some_table") as cursor:
                async for row in cursor:
                    ...


h = DbFunc()