import asyncio
import json
from time import sleep
# 웹 소켓 모듈을 선언한다.
import websockets
# 시리얼 통신에 필요
import serial

# **** 실행전에 터미널창에 [ docker run -p 6379:6379 -d redis:5 ] 입력 ****


# ----------------------------------------------------------------------------------------------//
# Python 웹소켓 서버에 접속에서 프롬프트 상에서 문자열을 입력받아 Python 웹소켓 서버에 전송하고
# 전송한 문자열에 대한 에코를 리턴 받는다.
# quit(종료) 문자를 입력받을 때까지 계속 웹소켓 연결되어 있다. quit 문자가 입력되면 접속이 자동으로 끊긴다.
# Python 웹소켓 서버는 파이참에서 실행중이다.
# ----------------------------------------------------------------------------------------------//

async def connect():

    # 웹 소켓에 접속.
    room_name = 'data'
    # ser = serial.Serial(
    #     port = 'COM7',
    #     baudrate = 115200,
    #     bytesize=serial.EIGHTBITS,
    #     timeout=1,
    # )
    async with websockets.connect("ws://localhost:8000/ws/" + room_name +"/") as websocket:
    # async with websockets.connect("ws://k6s105.p.ssafy.io:8004/ws/" + room_name +"/") as websocket:

        # str = input('웹소켓으로 전송할 내용을 입력[종료하려면 quit 입력!]: ')     # 사용자의 입력을 변수에 저장
        #print(str)  # 변수의 내용을 출력

        while 1:
            # while 1:
            #     data = ser.read(1)
            # quit가 들어오기 전까지 계속 입력받은 문자열을 전송하고 에코를 수신
            # await websocket.send(json.dumps({'message': 11, 'temp' : 11}))
            await websocket.send(json.dumps({'message': 'module_data', 'data' : "2334 828 2340 2431 2437 950 2381 2504 2529 2533 2536 2536 2532 2530 1389 2418 1686 2453 2509 1296 2237 2383 2366 2375 2463 2415 2406 2378 2474 2365 2377 2386 2378 2324 2374 2313 2314 2337 2347 2364 2336 2437 2443 2438 2437 1953 2442 2511 2531 2535 2539 2537 2533 2532 1610 2433 2365 2504 2520 2118 2474 1877 1099 2388 2462 2415 2408 2376 2472 2376 2386 2384 2376 2321 2378 2312 2315 2170 2335 2359 2331 2431 2441 2445 2436 1351 2407 2507 2532 2534 2538 2536 2534 2531 2342 2484 2481 2511 2517 1466 2431 2494 1780 2325 2461 2414 2408 2373 2474 2365 2379 2384 2376 2321 2373 2313 2316 2336 2343 2361 2337 2432 2442 2440 2438 1493 2414 2511 2530 2532 2535 2535 2532 2534 2079 2462 1379 2425 2230 1467 2426 2494 1800 2427 2468 2411 2402 2377 2477 2365 2385 2375 2372 2316 2375 2308 2311 2338 2343 2359 2334 2432 2444 2440 2436 2376 2480 2514 2522 2533 2536 2536 2531 2532 1666 2436 1212 2427 2371 1555 2141 2471 1154 2289 2457 2411 2403 2373 2475 2367 2384 2386 2378 2322 2374 2300 2315 2336 2346 2288 2324 2434 2442 2440 2436 2061 2449 2510 2529 2534 2535 2536 2532 2530 1899 2444 1835 2460 1837 1110 2407 2490 1745 2423 2463 2413 2406 2369 2474 2358 2379 2385 2371 2148 2365 2309 2309 2336 2345 2194 2333 829 2338 2432 2436 1727 2430 2508 2529 2536 2541 2537 2531 2532 2492 2497 1780 2455 2511 1710 1794 2448 1922 2041 2436 2412 2404 2369 2472 2381 2383 2385 2378 2321 2372 2312 2315 2335 2240 2353 2338 2437 2442 2441 2439 1482 2417 2509 2532 2534 2537 2536 2532 2532 2067 2462 2026 2476 2516 2146 2458 2416 1915 2429 2471 2411 2404 2373 2472 2375 2380 2389 2377 2325 2371 2241 2311 2335 2343 2355 2330 2430 2441 2439 2435 1279 2405 2507 2529 2534 2537 2538 2532 2530 2456 2458 1800 2254 2481 1038 2258 2478 1608 2414 2466 2412 2405 2375 2476 2379 2384 2384 2375 2280 2376 2305 2314 2336 2344 2359 2334 2433 2433 2440 2436 1103 2394 2504 2532 2535 2537 2535 2529 2531 1859 2217 1873 2458 1885 1722 1815 2447 1454 2272 2457 2414 2404 2373 2473 2376 2381 2386 2379 2321 2373 2311 2308 2336 2344 2359 2329 2427 2445 2441 2441 747 2375 2502 2526 2533 2536 2538 2534 2531 1698 2438 1469 2442 2431 1187 2413 2494 2352 1839 2422 2409 2403 2376 2476 2384 2383 2387 2375 2319 2264 2305 2312 2167 2329 2356 2331 2437 2441 1767 2388 2256 2467 2513 2532 2535 2538 2536 2531 2529 2118 2286 1115 2417 2508 1052 1791 2446 2288 1822 2422 2411 2405 2376 2477 2361 2383 2382 2373 2315 2374 2309 2308 2335 2338 2358"}))
            print('송신')
            sleep(12)
            # 웹 소켓 서버로 부터 메시지가 오면 콘솔에 출력
            # data = await websocket.recv()
            # print(data)
            # f.write(data)

            # str = input('웹소켓으로 전송할 내용을 입력[종료하려면 quit 입력!]: ')  # 사용자의 입력을 변수에 저장
            # print(str)  # 변수의 내용을 출력

        # f.close();


# 비동기로 서버에 접속한다.
asyncio.get_event_loop().run_until_complete(connect())