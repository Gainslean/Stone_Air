import asyncio
import aiohttp


async def stone():
    info = []
    escrow = []
    with open('wallet.txt', 'r', encoding='utf-8') as file:
        wallet = [line.strip() for line in file if line.strip()]

    for wallets in wallet:
        url = f"https://airdrop.stakestone.io/backend/airdrop/credentials?walletAddress={wallets}"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        a = int(float(data["tokenQualified"]))
                        print(f"Кошелек {wallets} = {a}")
                        if a > 0:
                            info.append(a)
                            escrow.append(wallets)

                    else:
                        error_text = await response.text()
                        print(f"Ошибка: {response.status} - {error_text}")
                        return None
            except Exception as e:
                print(f"Произошла ошибка: {str(e)}")
                return None
    print(sum(info))
    print(escrow)
