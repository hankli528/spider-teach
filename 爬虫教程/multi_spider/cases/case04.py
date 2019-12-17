import aiohttp
import asyncio
import ssl

async def fetch(session, url):
    async with session.get(url,ssl=ssl.SSLContext()) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session,'http://www.baidu.com')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())