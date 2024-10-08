import asyncio

import aiohttp


def user_json_to_plain_text(user: dict) -> str:
    user_text = (f'{user["name"]}, email: {user["email"]}\n'
                 f'Lives at {user["address"]["city"]} city, {user["address"]["street"]} street, {user["address"]["suite"]}')
    return user_text


async def json_response(session: aiohttp.ClientSession, url: str):
    # Plain version
    # response = await session.get(url)
    # response_json = await response.json()
    # return response_json

    # Concise version
    async with session.get(url) as response:
        json = await response.json()
        print('Awaited for url:', url)
        return json


async def get_users():
    base_url = 'https://jsonplaceholder.typicode.com/users'
    user_ids = range(1, 11)  # users/1, users/2, ... users/10
    async with aiohttp.ClientSession() as session:
        user_urls = [f'{base_url}/{user_id}' for user_id in user_ids]
        tasks = [asyncio.create_task(json_response(session, user_url)) for user_url in user_urls]
        return await asyncio.gather(*tasks)


async def print_all_users():
    users = await get_users()
    for idx, user in enumerate(users):
        print(f'User {idx}')
        print(user_json_to_plain_text(user))


async def main():
    await print_all_users()


if __name__ == '__main__':
    asyncio.run(main())
