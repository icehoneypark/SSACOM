import numpy as np
import sys 
arr = np.array([[2496, 787, 2324, 2352, 2450, 2463, 2468, 2494, 2511, 2527, 2530, 2528, 2521, 2515, 2489, 2503, 1556, 1883, 2447, 1948, 2458, 2502, 2498, 2476, 2442, 2413, 2404, 2402, 2344, 2388, 2365, 2330, 2354, 2320, 2366, 2324, 2329, 2329, 2328, 2323],
[2311, 2390, 2425, 2428, 2461, 2461, 2473, 2499, 2513, 2530, 2531, 2531, 2518, 2514, 2486, 2501, 1682, 2308, 2479, 1755, 2443, 2500, 2498, 2473, 2444, 2408, 2404, 2400, 2444, 2409, 2372, 2337, 2356, 2318, 2371, 2330, 2334, 2332, 2326, 2327],
[2308, 2394, 2422, 2425, 2299, 2457, 2473, 2500, 2515, 2531, 2534, 2530, 2521, 2514, 2490, 2505, 1285, 2407, 2491, 1525, 2429, 2500, 2500, 2479, 2445, 2409, 2416, 2407, 2451, 2411, 2373, 2333, 2357, 2315, 2369, 2329, 2333, 2331, 2331, 2326],
[2312, 2393, 2424, 2422, 2459, 2464, 2471, 2493, 2515, 2527, 2531, 2531, 2519, 2515, 2413, 2499, 910, 2335, 2395, 1059, 2405, 2498, 2501, 2475, 2441, 2411, 2410, 2403, 2446, 2411, 2375, 2337, 2357, 2323, 2368, 2333, 2330, 2327, 2331, 2328],
[2313, 2392, 2427, 2430, 2460, 2467, 2470, 2493, 2515, 2529, 2535, 2531, 2521, 2516, 2485, 2504, 908, 1140, 2316, 904, 2398, 2496, 2498, 2474, 2447, 2427, 2407, 2402, 2449, 2410, 2376, 1877, 2322, 2312, 2366, 2330, 2337, 2333, 2330, 2326],
[2309, 2384, 2426, 2427, 2460, 2465, 2475, 2499, 2514, 2530, 2534, 2532, 2522, 2514, 1902, 2459, 909, 2389, 2401, 912, 2396, 2492, 2495, 2477, 2444, 2407, 2408, 2400, 2449, 2408, 2376, 2336, 2359, 2319, 2367, 2326, 2336, 2331, 2332, 2327],
[2312, 2395, 2428, 2428, 2400, 2463, 2472, 2497, 2515, 2527, 2533, 2530, 2521, 2514, 2488, 2503, 915, 1539, 2076, 1488, 2429, 2500, 2499, 2477, 2445, 2410, 2410, 2409, 2449, 2391, 2368, 2222, 2349, 2314, 2367, 2329, 2337, 2334, 2333, 2322],
[2309, 2394, 2431, 2425, 2049, 2432, 2469, 2495, 2511, 2530, 2536, 2531, 2519, 2514, 2487, 2503, 966, 2389, 2349, 997, 2399, 2496, 2500, 2478, 2443, 2413, 2410, 2407, 1762, 2354, 2366, 2159, 2345, 2321, 2369, 2335, 2332, 2329, 2333, 2322],
[2307, 2393, 2428, 2431, 2457, 2463, 2472, 2494, 2514, 2530, 2534, 2529, 2516, 2514, 2485, 2500, 1108, 1787, 2443, 1145, 2408, 2495, 2498, 2475, 2445, 2409, 2410, 2401, 2451, 2409, 2371, 2337, 2358, 2319, 2369, 2331, 2334, 2331, 2329, 2329],
[2313, 2392, 2172, 2409, 2456, 2464, 2473, 2495, 2513, 2528, 2533, 2528, 2520, 2287, 2472, 2503, 917, 2298, 2484, 1930, 2457, 2498, 2501, 2478, 2443, 2406, 2407, 2404, 2282, 2400, 2370, 2336, 2358, 2321, 2369, 2329, 2337, 2337, 2334, 2326],
[2309, 2387, 2429, 2429, 2455, 2465, 2474, 2498, 2514, 2530, 2535, 2531, 2522, 2517, 2488, 2506, 1226, 2407, 2490, 926, 2399, 2500, 2497, 2477, 2443, 2425, 2412, 2401, 2447, 2409, 2365, 2336, 2362, 2315, 2372, 2329, 2337, 2331, 2327, 2326],
[2307, 2393, 2430, 2431, 2459, 2465, 2471, 2494, 2514, 2531, 2535, 2530, 2522, 2514, 2486, 2505, 1055, 2396, 1895, 878, 2399, 2497, 2499, 2479, 2443, 2409, 2415, 2402, 2452, 2409, 2370, 2335, 2354, 2319, 1909, 2294, 2328, 2329, 2334, 2331],
[2501, 770, 2319, 2410, 2454, 2458, 2470, 2495, 2514, 2532, 2521, 2529, 2518, 2518, 2485, 2507, 1684, 1704, 2435, 1516, 2430, 2500, 2495, 2473, 2442, 2406, 2406, 2405, 2448, 2408, 2374, 2336, 2358, 2316, 2366, 2327, 2332, 2330, 2330, 2324],
[2307, 2390, 2424, 2425, 2460, 2464, 2471, 2494, 2514, 2531, 2532, 2527, 2514, 2369, 2473, 2502, 1528, 2421, 1309, 841, 2393, 2494, 2497, 2479, 2441, 2406, 2407, 2402, 2446, 2410, 2376, 2339, 2360, 2322, 2366, 2334, 2335, 2326, 2328, 2332],
[2312, 2391, 2425, 2428, 2460, 2462, 2470, 2493, 2512, 2531, 2531, 2534, 2519, 2515, 2489, 2499, 915, 1619, 2378, 900, 2397, 2497, 2499, 2478, 2442, 2411, 2406, 2399, 2381, 2411, 2372, 2296, 2360, 2321, 2366, 2333, 2332, 2331, 2331, 2328],
[2314, 2390, 2424, 2427, 2460, 2465, 2471, 2494, 2513, 2532, 2535, 2526, 2517, 2512, 2484, 2501, 1285, 2212, 2353, 913, 2395, 2493, 2497, 2475, 2438, 2407, 2405, 2403, 2447, 2403, 2368, 2333, 2352, 2315, 2368, 2330, 2328, 2327, 2326, 2321],
[2303, 2390, 2423, 2267, 2288, 2449, 2468, 2491, 2514, 2527, 2533, 2529, 2517, 2514, 1894, 2453, 900, 2385, 2259, 891, 2396, 2494, 2496, 2474, 2441, 2407, 2405, 2400, 2451, 2408, 2083, 2313, 2351, 2319, 2367, 2327, 2329, 2326, 2327, 2323],
[2306, 2391, 2426, 2429, 2459, 2462, 2472, 2496, 2514, 2529, 2533, 2529, 2516, 2512, 1474, 2430, 915, 1843, 1733, 865, 2391, 2492, 2498, 2452, 2441, 2411, 2410, 2402, 2449, 2408, 2375, 2331, 2357, 2318, 2367, 2331, 2332, 2328, 2328, 2323],
[2309, 2389, 2426, 2425, 2455, 2461, 2470, 2492, 2514, 2526, 2529, 2527, 2519, 2512, 2399, 2496, 911, 2243, 2476, 1516, 2430, 2498, 2497, 2440, 2437, 2405, 2405, 2383, 2445, 2406, 2366, 2330, 2356, 2316, 2367, 2323, 1879, 2290, 2324, 2322],
[2311, 2388, 2424, 2365, 2449, 2462, 2471, 2492, 2509, 2526, 2528, 2532, 2520, 2511, 2489, 2504, 1686, 1804, 2443, 1513, 2433, 2501, 2500, 2474, 2446, 2409, 2412, 2405, 2448, 2406, 2371, 2289, 2353, 2318, 2366, 2325, 2328, 2329, 2314, 2328],
[2310, 2393, 2426, 1917, 2417, 2459, 2471, 2497, 2514, 2529, 2532, 2530, 2521, 2511, 2486, 2503, 1369, 1812, 2296, 1165, 2412, 2499, 2497, 2477, 2441, 2408, 2405, 2404, 2449, 2407, 2371, 2330, 2350, 2316, 2368, 2330, 2336, 2330, 2330, 2327],
[2309, 2390, 2425, 2432, 2458, 2469, 2474, 2497, 2514, 2527, 2531, 2529, 2520, 2515, 2485, 2506, 913, 2384, 1535, 857, 2393, 2492, 2496, 2476, 2333, 2399, 2403, 2402, 2448, 2407, 2342, 2332, 2352, 2316, 2368, 2326, 2331, 2332, 2328, 2320],
[2306, 2390, 2422, 2011, 2419, 2159, 2447, 2490, 2513, 2530, 2533, 2527, 2518, 2513, 2488, 2500, 1711, 2431, 2351, 1131, 2406, 2499, 2499, 2475, 2442, 2408, 2403, 2394, 2448, 2404, 2193, 1580, 2300, 2313, 2363, 2324, 2325, 2325, 2326, 2321],
[2311, 2387, 2427, 2429, 2453, 2458, 2470, 2492, 2513, 2527, 2530, 2529, 2518, 2511, 2487, 2504, 914, 2363, 1757, 867, 2391, 2492, 2499, 2475, 2439, 2407, 2404, 2400, 2444, 2404, 2369, 2335, 2351, 2313, 2368, 2324, 2332, 2328, 2327, 2317],
[2497, 776, 2325, 2412, 2454, 2461, 2469, 2493, 2511, 2530, 2531, 2530, 2517, 2510, 2489, 2504, 911, 2387, 2488, 920, 2398, 2495, 2498, 2477, 2442, 2408, 2407, 2398, 2186, 2386, 2364, 2333, 2356, 2317, 2366, 2322, 2330, 2329, 2334, 2330],
[2310, 2385, 2423, 2426, 2460, 2463, 2473, 2496, 2515, 2530, 2533, 2532, 2521, 2515, 2242, 2483, 900, 2298, 2223, 900, 2395, 2492, 2500, 2478, 2443, 2404, 2406, 2402, 2448, 2391, 2366, 2336, 2360, 2317, 2366, 2320, 2329, 2324, 2322, 2323],
[2306, 2384, 2421, 2425, 2297, 2456, 2467, 2493, 2511, 2527, 2528, 2529, 2520, 2514, 2484, 2502, 901, 2278, 2482, 916, 2395, 2493, 2498, 2475, 2441, 2404, 2404, 2401, 2447, 2406, 2366, 2327, 2356, 2319, 2366, 2326, 2330, 2324, 2328, 2318],
[2308, 2391, 2422, 2418, 2459, 2462, 2471, 2493, 2513, 2526, 2530, 2527, 2515, 2512, 2118, 2471, 907, 2224, 1886, 866, 2394, 2491, 2494, 2477, 2444, 2406, 2406, 2402, 2446, 2404, 2370, 2291, 2355, 2315, 2368, 2323, 2333, 2328, 2329, 2328],
[2315, 2392, 2425, 2268, 2193, 2442, 2471, 2497, 2511, 2533, 2531, 2530, 2520, 2516, 2488, 2501, 911, 2244, 1802, 1001, 2402, 2497, 2496, 2475, 2444, 2409, 2408, 2398, 2447, 2413, 2373, 2339, 2362, 2321, 2367, 2325, 2325, 2325, 2325, 2325],
[2311, 2393, 2428, 2322, 2447, 2460, 2470, 2493, 2513, 2531, 2533, 2530, 2516, 2514, 2487, 2502, 966, 1382, 2049, 1021, 2404, 2496, 2498, 2439, 2434, 2409, 2409, 2401, 2361, 2401, 2370, 2332, 1899, 2285, 2367, 2326, 2329, 2332, 2331, 2325],
[2310, 2392, 2426, 2428, 2455, 2462, 2471, 2495, 2515, 2530, 2535, 2530, 2517, 2510, 2491, 2504, 916, 2276, 2481, 937, 2398, 2494, 2497, 2466, 2444, 2410, 2405, 2403, 2445, 2409, 2370, 2333, 2359, 2317, 1628, 2278, 2336, 2330, 2332, 2321],
[2308, 2392, 2423, 2422, 2453, 2459, 2470, 2496, 2513, 2527, 2533, 2526, 2517, 2516, 2486, 2503, 1743, 2066, 1822, 1387, 2425, 2499, 2499, 2478, 2444, 2409, 2408, 2405, 2451, 2404, 2373, 2331, 2355, 2318, 1631, 2280, 2333, 2327, 2326, 2323],
[2315, 2392, 2429, 2369, 2453, 2461, 2470, 2495, 2511, 2529, 2532, 2529, 2518, 2514, 2484, 2504, 1554, 2424, 2249, 904, 2400, 2500, 2499, 2477, 2444, 2408, 2406, 2399, 2449, 2411, 2371, 2341, 2353, 2318, 2369, 2332, 2332, 2328, 2329, 2327],
[2312, 2394, 2426, 2426, 2457, 2464, 2470, 2495, 2510, 2530, 2533, 2527, 2519, 2512, 2489, 2507, 1144, 2348, 2485, 912, 2393, 2498, 2499, 2476, 2444, 2410, 2411, 2402, 2448, 2407, 2367, 2325, 2354, 2323, 2367, 2325, 2333, 2327, 2328, 2326],
[2308, 2391, 2425, 2430, 2457, 2466, 2475, 2498, 2513, 2528, 2535, 2531, 2520, 2513, 2489, 2503, 908, 2353, 2176, 899, 2395, 2493, 2495, 2475, 2442, 2413, 2409, 2402, 2447, 2410, 2377, 2339, 2352, 2313, 1908, 2288, 2331, 2324, 2324, 2324],
[2306, 2383, 2428, 2429, 2453, 2462, 2472, 2496, 2512, 2529, 2533, 2528, 2517, 2513, 2434, 2498, 912, 2386, 2487, 913, 2396, 2490, 2495, 2472, 2444, 2404, 2405, 2395, 2444, 2411, 2373, 2336, 2357, 2318, 2364, 2333, 2328, 2329, 2327, 2316],
[2495, 793, 2326, 1743, 2402, 2457, 2469, 2494, 2514, 2529, 2534, 2532, 2518, 2512, 2489, 2505, 1059, 2394, 2489, 1526, 2431, 2501, 2497, 2477, 2446, 2410, 2408, 2404, 2450, 2408, 2372, 2335, 2312, 2315, 2366, 2330, 2333, 2333, 2330, 2328],
[2310, 2392, 2424, 2429, 2459, 2464, 2476, 2495, 2511, 2533, 2533, 2528, 2520, 2514, 2487, 2503, 918, 2364, 2235, 901, 2395, 2492, 2499, 2476, 2443, 2411, 2409, 2403, 2450, 2410, 2373, 2334, 2357, 2315, 2368, 2330, 2337, 2334, 2324, 2326],
[2308, 2394, 2430, 2424, 2459, 2464, 2478, 2498, 2518, 2532, 2536, 2533, 2520, 2514, 2488, 2502, 911, 2389, 1962, 878, 2395, 2496, 2497, 2476, 2445, 2410, 2414, 2405, 2449, 2407, 2369, 2333, 2355, 2316, 2370, 2330, 2333, 2331, 2330, 2327],
[2312, 2389, 2424, 2428, 2458, 2465, 2474, 2499, 2515, 2522, 2531, 2533, 2517, 2510, 1311, 2423, 1275, 2404, 1244, 875, 2396, 2495, 2500, 2473, 2444, 2410, 2411, 2403, 2452, 2392, 2377, 2339, 2358, 2319, 2372, 2328, 2337, 2325, 2330, 2323],
[2305, 2389, 2423, 2428, 2460, 2463, 2470, 2495, 2513, 2531, 2536, 2530, 2518, 2513, 2488, 2508, 1410, 2253, 2480, 970, 2401, 2496, 2499, 2477, 2446, 2410, 2404, 2402, 2448, 2405, 2370, 2340, 2358, 2322, 2363, 2330, 2333, 2325, 2326, 2324],
[2313, 2393, 2428, 2013, 2421, 2460, 2473, 2493, 2510, 2527, 2533, 2532, 2518, 2512, 2488, 2506, 931, 1720, 2440, 941, 2402, 2498, 2498, 2479, 2443, 2412, 2409, 2401, 2384, 2393, 1628, 2285, 2357, 2318, 2366, 2331, 2332, 2333, 2330, 2327],
[2309, 2389, 2423, 2425, 2457, 2465, 2474, 2495, 2512, 2531, 2530, 2527, 2517, 2511, 2486, 2502, 1919, 1884, 2365, 1544, 2433, 2501, 2497, 2472, 2236, 2393, 2404, 2399, 2446, 2407, 2370, 2334, 2353, 2317, 2369, 2330, 2334, 2328, 2326, 2319],
[2311, 2388, 2426, 2430, 2457, 2462, 2475, 2499, 2515, 2531, 2531, 2529, 2518, 2514, 2123, 2474, 909, 2024, 2404, 1144, 2412, 2499, 2503, 2478, 2379, 2403, 2405, 2403, 2448, 2411, 1637, 2283, 2354, 2312, 2364, 2325, 2334, 2326, 2325, 2327],
[2313, 2391, 2422, 2389, 2455, 2460, 2470, 2495, 2512, 2527, 2531, 2531, 2516, 2514, 2484, 2504, 948, 2387, 1875, 879, 2396, 2499, 2499, 2475, 2442, 2405, 2405, 2401, 2446, 2404, 2374, 2336, 2359, 2316, 2058, 2304, 2328, 2328, 2335, 2325],
[2311, 2392, 2429, 2427, 2461, 2464, 2471, 2492, 2511, 2530, 2535, 2529, 2519, 2511, 2399, 2494, 914, 2365, 2398, 1141, 2406, 2496, 2497, 2477, 2442, 2407, 2410, 2402, 1745, 2347, 2364, 2330, 2352, 2315, 2371, 2332, 2334, 2333, 2329, 2326],
[2302, 2390, 2424, 2430, 2303, 2453, 2470, 2492, 2510, 2529, 2535, 2529, 2520, 2510, 2485, 2502, 910, 2300, 2116, 877, 2395, 2493, 2499, 2475, 2444, 2410, 2409, 2399, 2442, 2402, 2363, 2332, 2349, 2316, 2367, 2325, 2332, 2330, 2331, 2255],
[2307, 2390, 2423, 2426, 2459, 2461, 2470, 2494, 2515, 2530, 2534, 2529, 2518, 2514, 2483, 2501, 903, 2328, 1891, 872, 2394, 2493, 2497, 2476, 2445, 2407, 2408, 2400, 2451, 2395, 2367, 2335, 2353, 2315, 2364, 2325, 2333, 2329, 2324, 2326],
[2495, 780, 2324, 2412, 2454, 2463, 2471, 2497, 2514, 2528, 2533, 2530, 2517, 2512, 2488, 2503, 916, 2018, 2420, 956, 2400, 2349, 2485, 2473, 2443, 2406, 2407, 2399, 2446, 2408, 2377, 2337, 1628, 2264, 2363, 2328, 2334, 2332, 2327, 2321],
[2309, 2393, 2425, 2423, 2456, 2462, 2473, 2496, 2513, 2527, 2531, 2529, 2521, 2514, 2401, 2499, 926, 1793, 1815, 865, 2392, 2494, 2494, 2476, 2444, 2415, 2414, 2405, 2448, 2406, 2368, 2339, 2356, 2315, 2366, 2326, 2329, 2328, 2332, 2323],
[2308, 2388, 2425, 2426, 2460, 2463, 2470, 2496, 2515, 2529, 2536, 2532, 2518, 2514, 2486, 2506, 1282, 2406, 2472, 924, 2397, 2494, 2496, 2475, 2440, 2410, 2411, 2399, 2175, 2386, 2365, 2336, 2357, 2316, 2365, 2330, 2331, 2333, 2328, 2327],
[2306, 2391, 2425, 2429, 2459, 2466, 2472, 2495, 2512, 2530, 2532, 2530, 2520, 2514, 2485, 2504, 1204, 1675, 2435, 912, 2395, 2490, 2501, 2475, 2443, 2409, 2405, 2400, 2384, 2406, 2368, 2331, 1622, 2263, 2074, 2303, 2334, 2331, 2332, 2324],
[2309, 2391, 2426, 2427, 2457, 2463, 2472, 2494, 2513, 2530, 2531, 2531, 2520, 2514, 2484, 2502, 1744, 2287, 2483, 916, 2394, 2495, 2497, 2477, 1842, 2360, 2400, 2400, 2450, 2410, 2369, 2335, 2359, 2322, 2367, 2331, 2340, 2335, 2337, 2330],
[2312, 2394, 2428, 1656, 2401, 2460, 2471, 2495, 2514, 2529, 2533, 2530, 2517, 2510, 2488, 2509, 1770, 2436, 2492, 1343, 2424, 2500, 2497, 2475, 2439, 2410, 2411, 2399, 2448, 2390, 2367, 2331, 2359, 2314, 2370, 2331, 2332, 2326, 2327, 2322],
[2310, 2391, 2428, 2329, 2449, 2464, 2473, 2497, 2515, 2531, 2533, 2530, 2518, 2511, 2487, 2503, 997, 2391, 2486, 1001, 2404, 2501, 2499, 2475, 2443, 2410, 2405, 2403, 2449, 2411, 2373, 2335, 2248, 2307, 2368, 2329, 2333, 2326, 2333, 2325],
[2310, 2394, 2428, 2427, 2399, 2461, 2470, 2497, 2510, 2532, 2534, 2532, 2518, 2513, 2488, 2504, 970, 2252, 2339, 905, 2399, 2493, 2498, 2479, 2444, 2409, 2408, 2401, 2444, 2396, 2366, 2334, 2354, 2320, 2371, 2326, 2333, 2331, 2329, 2330],
[2311, 2388, 2429, 2427, 2455, 2464, 2472, 2497, 2514, 2533, 2531, 2528, 2521, 2518, 2487, 2502, 1051, 2397, 2414, 913, 2396, 2496, 2498, 2479, 2444, 2411, 2407, 2401, 2448, 2409, 2371, 2331, 2354, 2322, 2366, 2297, 2339, 2329, 2333, 2324],
[2308, 2390, 2423, 2424, 2204, 2440, 2470, 2494, 2509, 2532, 2534, 2528, 2517, 2514, 2489, 2505, 911, 2300, 1863, 878, 2395, 2495, 2498, 2477, 2440, 2410, 2407, 2400, 2031, 2374, 2368, 2341, 2355, 2317, 2368, 2332, 2333, 2328, 2330, 2322],
[2308, 2391, 2427, 2425, 2457, 2463, 2471, 2495, 2511, 2525, 2531, 2529, 2520, 2512, 2487, 2504, 907, 2387, 2465, 969, 2403, 2496, 2500, 2477, 2448, 2407, 2409, 2404, 2448, 2411, 2373, 2337, 2362, 2309, 2370, 2332, 2328, 1885, 2297, 2327],
[2310, 2390, 2425, 2423, 2460, 2461, 2471, 2496, 2513, 2528, 2532, 2529, 2516, 2513, 2490, 2504, 917, 2386, 1861, 1471, 2428, 2498, 2495, 2475, 2443, 2408, 2411, 2400, 2447, 2395, 2367, 2333, 2353, 2320, 2366, 2331, 2332, 2328, 2329, 2321],
[2494, 786, 2324, 2411, 2458, 2462, 2471, 2497, 2514, 2531, 2534, 2530, 2522, 2514, 2465, 2503, 912, 2386, 2122, 886, 2393, 2496, 2445, 2472, 2444, 2409, 2407, 2401, 2449, 2392, 2372, 2334, 2351, 2320, 2368, 2328, 2332, 2329, 2335, 2328],
[2314, 2393, 2427, 2426, 2461, 2464, 2476, 2496, 2510, 2530, 2533, 2528, 2520, 2511, 2485, 2502, 1286, 2407, 1901, 1106, 2406, 2497, 2494, 2477, 2447, 2410, 2404, 2401, 2448, 2410, 2267, 2327, 2356, 2318, 2371, 2330, 2337, 2334, 2328, 2322],
[2309, 2391, 2425, 2330, 2449, 2464, 2473, 2497, 2516, 2528, 2532, 2530, 2520, 2516, 2490, 2504, 1199, 1805, 2447, 1540, 2428, 2501, 2501, 2475, 2443, 2410, 2409, 2404, 2448, 2392, 2370, 2335, 2356, 2320, 2364, 2329, 2336, 2336, 2331, 2327],
[2311, 2390, 2428, 2429, 2463, 2467, 2476, 2497, 2514, 2527, 2530, 2531, 2519, 2513, 2487, 2505, 1177, 1582, 2433, 1513, 2432, 2498, 2500, 2179, 1984, 2370, 2402, 2405, 2447, 2410, 2302, 2334, 2358, 2324, 2368, 2332, 2337, 2336, 2335, 2326],
[2308, 2390, 2428, 2427, 2209, 2446, 2471, 2496, 2517, 2531, 2533, 2531, 2520, 2516, 2488, 2502, 1253, 2368, 2489, 912, 2395, 2494, 2495, 2474, 2000, 2371, 2403, 2402, 2447, 2411, 2371, 2336, 2359, 2315, 2369, 2329, 2332, 2325, 2330, 2318],
[2316, 2390, 2425, 2016, 2420, 2462, 2472, 2490, 2511, 2528, 2532, 2527, 2520, 2515, 2486, 2502, 954, 2386, 2397, 907, 2399, 2494, 2498, 2473, 2441, 2412, 2409, 2396, 2446, 2407, 2367, 2331, 2357, 2316, 2372, 2330, 2336, 2333, 2327, 2326],
[2306, 2388, 2426, 2425, 2456, 2460, 2471, 2498, 2514, 2534, 2533, 2531, 2522, 2514, 2490, 2503, 917, 2385, 2400, 1576, 2436, 2499, 2495, 2474, 2448, 2409, 2412, 2401, 2448, 2391, 2362, 2335, 2359, 2320, 2366, 2326, 2333, 2326, 2324, 2216],
[2302, 2394, 2429, 1758, 2406, 2460, 2471, 2496, 2513, 2529, 2533, 2531, 2520, 2512, 2488, 2504, 917, 1792, 2377, 1003, 2402, 2498, 2500, 2474, 2442, 2410, 2408, 2404, 2446, 2392, 2369, 2337, 2355, 2317, 2368, 2288, 2336, 2331, 2329, 2326],
[2309, 2391, 2427, 2425, 2459, 2465, 2475, 2498, 2514, 2530, 2532, 2528, 2518, 2515, 2467, 2503, 903, 2158, 2473, 927, 2397, 2496, 2497, 2480, 2444, 2408, 2410, 2402, 2445, 2408, 2369, 2337, 2350, 2310, 2365, 2329, 2330, 2332, 2332, 2327],
[2305, 2389, 2424, 2428, 2456, 2461, 2472, 2497, 2514, 2527, 2530, 2531, 2520, 2515, 2261, 2487, 1305, 2409, 1177, 833, 2389, 2492, 2495, 2477, 2445, 2409, 2408, 2402, 2279, 2385, 1908, 2300, 2354, 2318, 2366, 2330, 2336, 2331, 2330, 2324],
[2314, 2393, 2426, 2429, 2459, 2464, 2474, 2497, 2516, 2529, 2533, 2529, 2517, 2512, 2486, 2501, 1423, 2417, 2492, 919, 2397, 2495, 2498, 2477, 2445, 2410, 2413, 2403, 2343, 2400, 2371, 2332, 2351, 2323, 2370, 2333, 2333, 2328, 2328, 2325],
[2313, 2395, 2431, 2431, 2462, 2465, 2471, 2495, 2518, 2531, 2536, 2530, 2519, 2513, 2486, 2505, 1755, 2433, 2268, 2164, 2454, 2501, 2498, 2476, 2440, 2408, 2408, 2402, 2448, 2410, 2372, 2336, 2362, 2320, 2370, 2331, 2332, 2330, 2329, 2328],
[2502, 787, 2320, 2417, 2454, 2461, 2473, 2493, 2513, 2530, 2534, 2526, 2514, 2512, 2487, 2503, 908, 2384, 2345, 907, 2396, 2495, 2499, 2326, 1731, 2356, 2402, 2399, 2319, 2398, 2372, 2338, 2360, 2320, 2369, 2331, 2331, 2261, 2327, 2325],
[2310, 2393, 2430, 2423, 2457, 2464, 2476, 2494, 2514, 2529, 2534, 2530, 2519, 2489, 2484, 2504, 964, 1968, 2447, 1298, 2414, 2499, 2499, 2480, 2445, 2409, 2408, 2400, 2450, 2393, 2367, 2336, 2359, 2318, 2366, 2326, 2333, 2330, 2328, 2321],
[2313, 2391, 2426, 2267, 2445, 2463, 2473, 2496, 2516, 2530, 2531, 2531, 2519, 2511, 2487, 2501, 1823, 1850, 2448, 1153, 2410, 2502, 2497, 2477, 2440, 2407, 2406, 2401, 2449, 2395, 2361, 2335, 2354, 2318, 2369, 2328, 2329, 2336, 2326, 232],
[2312, 2392, 2426, 2431, 2457, 2464, 2475, 2498, 2513, 2526, 2532, 2531, 2521, 2516, 2487, 2505, 996, 2391, 2431, 999, 2398, 2493, 2497, 2474, 2444, 2428, 2408, 2403, 2448, 2406, 2370, 2339, 2359, 2320, 2367, 2329, 2333, 2328, 2330, 2327],
[2302, 2395, 2425, 2424, 2460, 2405, 2470, 2496, 2514, 2530, 2533, 2531, 2520, 2515, 2487, 2499, 918, 2332, 2393, 1278, 2418, 2499, 2502, 2476, 1734, 2359, 2398, 2399, 2441, 2393, 2367, 2335, 2359, 2319, 2368, 2331, 2337, 2330, 2330, 2325],
[2316, 2390, 2426, 2430, 2458, 2466, 2475, 2493, 2512, 2529, 2534, 2530, 2519, 2509, 2489, 2506, 918, 2298, 2032, 882, 2392, 2495, 2495, 2472, 2443, 2407, 2404, 2400, 1740, 2355, 2361, 2329, 2355, 2315, 2325, 2323, 2331, 2330, 2324, 2321],
[2310, 2387, 2428, 2421, 2458, 2463, 2467, 2493, 2513, 2529, 2532, 2530, 2521, 2512, 2486, 2501, 1145, 2365, 2121, 947, 2399, 2494, 2500, 2474, 2441, 2408, 2408, 2402, 2452, 2407, 2326, 2331, 2247, 2307, 2192, 2311, 2333, 2330, 2327, 2321],
[2310, 2392, 2425, 2011, 2418, 2466, 2471, 2496, 2515, 2530, 2533, 2531, 2523, 2514, 2489, 2505, 1576, 2314, 2389, 930, 2395, 2496, 2495, 2475, 2443, 2411, 2409, 2404, 2445, 2410, 2373, 2338, 2355, 2314, 2369, 2329, 2336, 2335, 2332, 2327],
[2316, 2394, 2426, 2015, 2366, 2462, 2473, 2496, 2513, 2530, 2535, 2532, 2521, 2520, 2491, 2504, 1413, 2414, 2493, 1551, 2429, 2498, 2500, 2475, 2402, 2403, 2406, 2401, 2451, 2395, 2366, 2337, 2360, 2319, 2368, 2327, 2333, 2326, 2325, 2323],
[2308, 2392, 2427, 2424, 2459, 2370, 2465, 2497, 2514, 2530, 2533, 2533, 2520, 2518, 2489, 2489, 916, 2388, 2483, 917, 2396, 2495, 2497, 2477, 2444, 2407, 2405, 2400, 1750, 2356, 2361, 2337, 2358, 2320, 2371, 2329, 2334, 2331, 2331, 2328],
[2311, 2394, 2426, 2427, 2458, 2464, 2471, 2496, 2505, 2529, 2533, 2532, 2519, 2516, 2488, 2501, 1291, 2322, 2342, 1225, 2416, 2498, 2497, 2479, 2444, 2411, 2409, 2405, 2444, 2410, 2372, 2335, 2354, 2319, 2364, 2331, 2338, 2226, 2323, 2322],
[2303, 2383, 2424, 2427, 2458, 2465, 2473, 2495, 2515, 2528, 2535, 2530, 2518, 2513, 2487, 2499, 997, 2389, 2487, 961, 2399, 2496, 2499, 2479, 2444, 2407, 2409, 2401, 2450, 2406, 2372, 2338, 2329, 2309, 2360, 2326, 2335, 2333, 2328, 2329],
[2500, 777, 2326, 2348, 2453, 2462, 2473, 2493, 2512, 2528, 2533, 2531, 2521, 2514, 2490, 2505, 1207, 2261, 2475, 914, 2394, 2495, 2358, 2463, 2442, 2409, 2407, 2402, 1204, 2324, 2356, 2332, 1898, 2282, 2194, 2312, 2338, 2332, 2330, 2325],
[2309, 2390, 2427, 2423, 2461, 2465, 2473, 2497, 2514, 2530, 2534, 2532, 2520, 2517, 2487, 2501, 1499, 2139, 2106, 2271, 2486, 2504, 2498, 2477, 2269, 2399, 2406, 2398, 2449, 2409, 2374, 2335, 2353, 2319, 2369, 2329, 2333, 2324, 2327, 2326],
[1998, 2367, 2425, 2429, 2460, 2467, 2471, 2496, 2514, 2528, 2532, 2532, 2519, 2513, 2488, 2508, 1918, 2303, 2455, 1004, 2405, 2498, 2499, 2480, 2443, 2407, 2406, 2402, 2409, 2393, 2367, 2339, 2357, 2316, 2367, 2331, 2336, 2336, 2328, 2332],
[2313, 2395, 2430, 2427, 2461, 2469, 2473, 2499, 2513, 2530, 2533, 2531, 2517, 2516, 2489, 2503, 1663, 2397, 2488, 1124, 2407, 2499, 2500, 2477, 2445, 2410, 2403, 2403, 2197, 2368, 2362, 2334, 2353, 2317, 2368, 2327, 2328, 2330, 2324, 2321],
[2310, 2388, 2427, 2427, 2455, 2464, 2475, 2498, 2515, 2530, 2533, 2531, 2519, 2516, 2452, 2500, 945, 1791, 2303, 901, 2392, 2495, 2495, 2477, 2444, 2412, 2409, 2405, 2450, 2409, 2374, 2333, 2352, 2318, 2368, 2328, 2331, 2332, 2331, 2324],
[2312, 2392, 2431, 2425, 2456, 2466, 2473, 2497, 2516, 2530, 2530, 2531, 2521, 2513, 2486, 2502, 913, 2022, 2456, 917, 2395, 2497, 2498, 2474, 2446, 2411, 2412, 2403, 2446, 2409, 2367, 2337, 2361, 2322, 2370, 2330, 2331, 2335, 2329, 2327],
[2309, 2388, 2429, 2425, 2453, 2461, 2473, 2498, 2513, 2531, 2532, 2530, 2520, 2512, 1904, 2455, 907, 2245, 2390, 905, 2399, 2495, 2495, 2479, 2446, 2409, 2409, 2404, 2020, 2372, 2369, 2333, 2351, 2321, 2365, 2329, 2334, 2330, 2332, 2324],
[2313, 2390, 2423, 2427, 2458, 2462, 2471, 2493, 2513, 2532, 2535, 2532, 2516, 2513, 2486, 2502, 1520, 2419, 2407, 1980, 2462, 2502, 2499, 2477, 2378, 2404, 2412, 2402, 1507, 2343, 2361, 2333, 2354, 2320, 2370, 2331, 2333, 2328, 2326, 2315],
[2315, 2390, 2425, 2427, 2458, 2468, 2473, 2493, 2513, 2532, 2535, 2530, 2521, 2513, 2488, 2504, 1640, 2428, 2493, 2202, 2475, 2506, 2500, 2476, 2443, 2422, 2407, 2401, 2341, 2388, 2369, 2334, 2357, 2320, 2368, 2333, 2332, 2329, 2326, 2321],
[2308, 2392, 2427, 2429, 2459, 2465, 2473, 2498, 2515, 2528, 2532, 2531, 2516, 2511, 2488, 2504, 2410, 1898, 2453, 1200, 2413, 2498, 2498, 2476, 2442, 2409, 2405, 2402, 1734, 2352, 2363, 2343, 2354, 2314, 2364, 2329, 2327, 2329, 2331, 2324],
[2311, 2390, 2425, 2426, 2456, 2429, 2469, 2494, 2512, 2531, 2532, 2529, 2519, 2511, 2489, 2507, 1057, 2334, 2482, 1521, 2431, 2501, 2127, 2447, 1711, 2343, 2399, 2395, 2094, 2380, 2079, 2309, 2238, 2309, 2365, 2327, 2328, 2323, 2324, 2318],
[2312, 2390, 2426, 2429, 2456, 2466, 2473, 2496, 2512, 2529, 2533, 2528, 2519, 2511, 2431, 2498, 1048, 1805, 2443, 937, 2395, 2495, 2499, 2476, 1707, 2353, 2400, 2398, 2446, 2394, 2364, 2334, 2354, 2317, 2368, 2322, 2333, 2326, 2328, 2327],
[2498, 777, 2323, 2412, 2052, 2432, 2468, 2497, 2514, 2531, 2533, 2532, 2521, 2514, 2489, 2505, 2107, 1582, 2430, 1614, 2432, 2500, 2499, 2474, 2444, 2407, 2403, 2402, 1492, 2331, 2362, 2333, 2355, 2310, 2366, 2324, 2332, 2326, 2329, 2320],
[2312, 2393, 2425, 2426, 2457, 2461, 2473, 2501, 2514, 2531, 2537, 2534, 2517, 2514, 2488, 2505, 1051, 2255, 2478, 998, 2397, 2498, 2495, 2471, 1761, 2357, 2399, 2396, 2446, 2408, 2366, 2335, 2353, 2311, 2368, 2324, 2329, 2325, 2328, 2323],
[2307, 2385, 2421, 2423, 2355, 2456, 2472, 2496, 2511, 2529, 2533, 2530, 2520, 2514, 2486, 2501, 1029, 1768, 2407, 900, 2395, 2494, 2497, 2474, 2436, 2406, 2409, 2398, 2444, 2407, 1627, 2281, 2353, 2317, 2257, 2321, 2327, 2290, 2320, 2319],
[2307, 2385, 2427, 2269, 2444, 2464, 2470, 2493, 2514, 2531, 2532, 2530, 2517, 2514, 2487, 2500, 928, 2388, 2258, 901, 2396, 2497, 2498, 2478, 2444, 2409, 2408, 2402, 2450, 2408, 1910, 2300, 2358, 2314, 1904, 2289, 2335, 2324, 2326, 2324],
[2310, 2395, 2429, 2426, 2458, 2462, 2471, 2495, 2514, 2529, 2532, 2531, 2520, 2513, 2449, 2500, 939, 2388, 2483, 912, 2394, 2496, 2496, 2473, 2440, 2407, 2407, 1683, 2390, 2400, 2367, 2337, 2294, 2310, 2366, 2327, 2330, 2329, 2333, 2330],
[2315, 2390, 2425, 2427, 2460, 2465, 2473, 2496, 2517, 2531, 2532, 2531, 2518, 2514, 2343, 2491, 1525, 2416, 2439, 918, 2393, 2493, 2496, 2473, 1726, 2370, 2400, 2401, 2448, 1953, 2332, 2326, 2355, 2319, 2365, 2331, 2326, 2324, 2327, 2325],
[2307, 2391, 2425, 2425, 2458, 2466, 2473, 2494, 2512, 2531, 2534, 2529, 2520, 2516, 2486, 2504, 2388, 2482, 2272, 906, 2398, 2493, 2495, 2475, 2442, 2409, 2410, 2403, 2144, 2388, 2368, 2331, 2355, 2315, 2340, 2329, 2332, 2331, 2327, 2325],
[2308, 2389, 2423, 2388, 2451, 2458, 2474, 2498, 2515, 2530, 2531, 2531, 2518, 2513, 2486, 2502, 911, 1656, 2435, 995, 2399, 2496, 2499, 2478, 2277, 2414, 2406, 2403, 1857, 2363, 2365, 2331, 2360, 2316, 2324, 2316, 2328, 2329, 2326, 2319],
[2307, 2390, 2426, 2420, 2456, 2464, 2474, 2496, 2513, 2529, 2532, 2531, 2518, 2514, 2485, 2503, 1624, 1776, 2441, 1783, 2443, 2499, 2496, 2472, 2404, 2404, 2405, 2398, 2354, 2399, 2362, 2308, 2287, 2314, 2254, 2320, 2324, 2328, 2329, 2326],
[2307, 2391, 2427, 1758, 2409, 2464, 2472, 2495, 2513, 2531, 2533, 2526, 2517, 2514, 2489, 2503, 1512, 1967, 2457, 1053, 2408, 2500, 2497, 2474, 2439, 2412, 2413, 2404, 2448, 2408, 2374, 2337, 2359, 2322, 2369, 2330, 2332, 2334, 2330, 2330],
[2306, 2391, 2425, 2428, 2459, 2461, 2470, 2495, 2513, 2531, 2533, 2530, 2520, 2513, 2486, 2501, 1012, 2245, 2476, 978, 2400, 2498, 2498, 2478, 2269, 2405, 2408, 2401, 2022, 2355, 2367, 2332, 2356, 2321, 2369, 2331, 2333, 2329, 2329, 2325],
[2301, 2393, 2427, 2431, 2462, 2467, 2474, 2499, 2517, 2532, 2535, 2531, 2522, 2516, 2488, 2506, 933, 1657, 2434, 915, 2394, 2493, 2496, 2476, 2445, 2405, 2407, 2401, 2450, 2407, 2370, 2331, 2351, 2319, 2366, 2328, 2330, 2328, 2328, 2321],
[2495, 773, 2318, 2416, 2458, 2464, 2472, 2496, 2513, 2529, 2535, 2530, 2516, 2512, 2488, 2500, 1205, 2119, 2464, 1742, 2444, 2501, 2499, 2475, 2443, 2411, 2406, 2401, 2281, 2398, 2192, 2319, 2349, 2318, 2365, 2326, 2331, 2328, 2326, 2326],
[2306, 2391, 2425, 2423, 2457, 2461, 2472, 2498, 2516, 2528, 2537, 2532, 2518, 2517, 2487, 2503, 926, 1799, 2444, 1519, 2430, 2496, 2498, 2474, 2441, 2413, 2410, 2406, 2449, 2409, 2377, 2338, 2362, 2321, 2366, 2330, 2336, 2336, 2328, 2323],
[2311, 2392, 2428, 2428, 2458, 2463, 2468, 2492, 2515, 2526, 2530, 2530, 2520, 2514, 2485, 2506, 916, 2362, 2484, 914, 2397, 2493, 2497, 2475, 2444, 2404, 2405, 2398, 2015, 2361, 2364, 2333, 2353, 2317, 2368, 2328, 2339, 2332, 2327, 2323],
[2311, 2390, 2428, 2427, 2457, 2466, 2474, 2493, 2510, 2529, 2533, 2529, 2519, 2514, 2486, 2503, 910, 2391, 2261, 887, 2395, 2493, 2500, 2230, 2421, 2407, 2406, 2402, 2450, 2403, 2374, 2339, 1622, 2266, 2370, 2327, 2333, 2328, 2321, 2326],
[2040, 2362, 2426, 2423, 2456, 2462, 2472, 2494, 2513, 2530, 2535, 2529, 2518, 2513, 2488, 2505, 915, 2386, 2430, 1518, 2433, 2500, 2500, 2472, 2444, 2410, 2406, 2405, 2282, 2380, 2366, 2328, 2358, 2318, 2369, 2310, 2331, 2329, 2332, 2325],
[2311, 2386, 2427, 1761, 2404, 2462, 2473, 2496, 2514, 2528, 2533, 2531, 2521, 2515, 2490, 2503, 1973, 2358, 2484, 1323, 2424, 2500, 2500, 2439, 2009, 2375, 2401, 2403, 2010, 2373, 2369, 2336, 2364, 2325, 2368, 2333, 2337, 2334, 2331, 2324],
[2314, 2392, 2430, 2429, 2461, 2466, 2471, 2493, 2513, 2530, 2535, 2528, 2520, 2513, 2485, 2504, 2353, 2215, 2478, 1081, 2407, 2497, 2496, 2477, 2443, 2408, 2413, 2401, 2451, 2403, 2367, 2338, 2313, 2309, 2367, 2329, 2334, 2329, 2327, 2327],
[2313, 2393, 2425, 2389, 2454, 2463, 2466, 2497, 2514, 2529, 2535, 2531, 2518, 2285, 2473, 2505, 2300, 2477, 2498, 1542, 2431, 2503, 2497, 2476, 2443, 2409, 2408, 2397, 1983, 2370, 2361, 2329, 2352, 2319, 2368, 2332, 2331, 2327, 2329, 2319],
[2312, 2395, 2422, 2425, 2459, 2462, 2471, 2495, 2514, 2528, 2533, 2530, 2520, 2424, 2480, 2504, 902, 2335, 2480, 934, 2397, 2495, 2496, 2476, 2336, 2402, 2407, 2401, 2450, 2407, 2366, 2332, 2356, 2321, 2365, 2330, 2338, 2333, 2332, 2323],
[2312, 2389, 2426, 2426, 2461, 2463, 2472, 2499, 2513, 2531, 2535, 2531, 2516, 2513, 2488, 2503, 1279, 2406, 2126, 1579, 2430, 2502, 2497, 2477, 2443, 2407, 2408, 2399, 2444, 2393, 2371, 2338, 2357, 2316, 2368, 2332, 2334, 2327, 2326, 2324],
[2314, 2391, 2425, 2429, 2458, 2462, 2471, 2494, 2514, 2528, 2531, 2528, 2519, 2512, 2486, 2504, 917, 1792, 2442, 1546, 2436, 2500, 2501, 2477, 2441, 2409, 2405, 2401, 2450, 2407, 2373, 2342, 2358, 2318, 2370, 2332, 2333, 2329, 2332, 2321],
[2313, 2393, 2424, 2429, 2460, 2465, 2473, 2500, 2514, 2531, 2533, 2532, 2520, 2513, 2259, 2489, 915, 2384, 2485, 918, 2394, 2497, 2498, 2479, 2445, 2409, 2408, 2404, 2446, 2353, 2364, 2330, 2355, 2313, 2368, 2325, 2330, 2330, 2328, 2326],
[2502, 775, 2323, 2414, 2455, 2462, 2469, 2500, 2514, 2530, 2532, 2526, 2516, 2476, 2484, 2502, 1058, 1801, 1856, 861, 2395, 2493, 2497, 2474, 2333, 2397, 2406, 2396, 2444, 2410, 2373, 2336, 2362, 2320, 2369, 2327, 2330, 2325, 2322, 2322],
[2309, 2393, 2424, 2428, 2455, 2461, 2474, 2496, 2512, 2528, 2532, 2531, 2518, 2515, 2486, 2501, 1944, 2449, 2493, 1414, 2426, 2499, 2498, 2475, 2441, 2408, 2409, 2402, 2444, 2394, 2367, 2333, 2357, 2317, 2369, 2328, 2329, 2328, 2332, 2327],
[2309, 2391, 2429, 2431, 2453, 2463, 2474, 2495, 2514, 2532, 2532, 2528, 2517, 2514, 2487, 2501, 1553, 2419, 2491, 1067, 2404, 2499, 2495, 2476, 2441, 2408, 2410, 2398, 2446, 2388, 2366, 2334, 1628, 2266, 2362, 2325, 2331, 2327, 2324, 2323],
[2306, 2390, 2423, 2428, 2458, 2464, 2474, 2495, 2512, 2529, 2534, 2529, 2521, 2513, 2484, 2503, 933, 2386, 2488, 1751, 2445, 2500, 2500, 2477, 2445, 2408, 2408, 2411, 2452, 2395, 2370, 2339, 2249, 2316, 2370, 2330, 2340, 2337, 2334, 2327],
[2307, 2393, 2431, 2265, 2445, 2465, 2474, 2496, 2515, 2531, 2533, 2529, 2520, 2516, 2489, 2503, 1764, 2295, 2484, 1549, 2435, 2500, 2500, 2477, 2003, 2368, 2406, 2399, 2178, 2384, 2362, 2337, 2357, 2320, 2365, 2324, 2335, 2327, 2325, 2324],
[2310, 2393, 2426, 2426, 2456, 2467, 2474, 2501, 2514, 2530, 2534, 2530, 2519, 2514, 2488, 2507, 2282, 2252, 2480, 1984, 2456, 2503, 2499, 2475, 2443, 2409, 2411, 2402, 2448, 2410, 2368, 2336, 2360, 2321, 2365, 2325, 2334, 2332, 2329, 2323],
[2306, 2397, 2429, 2431, 2458, 2468, 2475, 2498, 2514, 2530, 2534, 2531, 2518, 2492, 2489, 2507, 2445, 2256, 2481, 959, 2400, 2499, 2500, 2477, 2445, 2408, 2410, 2403, 2447, 2393, 2369, 2336, 2358, 2318, 2367, 2327, 2332, 2332, 2327, 2322],
[2315, 2394, 2431, 2430, 2459, 2466, 2471, 2497, 2512, 2528, 2535, 2530, 2520, 2514, 2486, 2506, 950, 1723, 2437, 909, 2397, 2494, 2497, 2479, 2441, 2411, 2404, 2405, 2447, 2409, 2371, 2331, 2355, 2314, 2364, 2329, 2333, 2329, 2329, 2323],
[2306, 2387, 2426, 2426, 2456, 2462, 2471, 2494, 2511, 2527, 2533, 2532, 2520, 2515, 2487, 2503, 1056, 1833, 2359, 900, 2396, 2494, 2410, 2467, 1734, 2355, 2400, 2398, 2447, 2404, 2372, 2339, 2355, 2319, 2371, 2330, 2335, 2328, 2329, 2325],
[2310, 2390, 2424, 2427, 2457, 2469, 2472, 2497, 2516, 2529, 2534, 2531, 2520, 2516, 2488, 2504, 1520, 1099, 2401, 900, 2396, 2494, 2497, 2476, 2444, 2405, 2405, 2398, 2446, 2404, 2372, 2334, 2358, 2317, 2079, 2302, 2333, 2329, 2325, 2325],
[2309, 2392, 2426, 2428, 2461, 2465, 2475, 2495, 2512, 2531, 2535, 2530, 2520, 2514, 2348, 2491, 919, 2383, 2488, 920, 2400, 2496, 2500, 2476, 2445, 2412, 2413, 2400, 2448, 2410, 2372, 2333, 2354, 2315, 2082, 2306, 2332, 2324, 2328, 2328],
[2314, 2395, 2428, 2431, 2459, 2463, 2470, 2495, 2514, 2530, 2533, 2530, 2519, 2513, 2489, 2507, 1097, 2396, 2488, 939, 2397, 2496, 2498, 2478, 2380, 2408, 2409, 2397, 2446, 2409, 2377, 2337, 2356, 2318, 2370, 2333, 2336, 2332, 2330, 2326],
[2500, 785, 2323, 2412, 2456, 2463, 2471, 2492, 2514, 2530, 2532, 2529, 2517, 2512, 2484, 2501, 1055, 2341, 2482, 1522, 2429, 2502, 2497, 2474, 2444, 2407, 2406, 2401, 2450, 2408, 2370, 2339, 2355, 2318, 2373, 2334, 2335, 2332, 2329, 2321],
[2311, 2392, 2427, 2430, 2458, 2464, 2474, 2496, 2515, 2529, 2533, 2531, 2519, 2511, 2485, 2503, 1052, 2026, 1644, 999, 2397, 2492, 2499, 2452, 2436, 2406, 2404, 2403, 2449, 2394, 2368, 2335, 2353, 2318, 2371, 2329, 2329, 2332, 2332, 2327],
[2316, 2390, 2430, 2428, 2459, 2465, 2472, 2496, 2511, 2534, 2533, 2530, 2522, 2516, 2124, 2476, 2032, 2429, 2495, 1578, 2437, 2493, 2501, 2474, 1554, 2344, 2401, 2399, 2444, 2397, 2371, 2335, 2359, 2317, 2370, 2335, 2334, 2332, 2329, 2325],
[2310, 2395, 2429, 2425, 2458, 2462, 2471, 2495, 2512, 2529, 2533, 2533, 2519, 2516, 2486, 2504, 1480, 2278, 2483, 1184, 2411, 2498, 2498, 2477, 2446, 2414, 2414, 2403, 2448, 2408, 2375, 2336, 2361, 2319, 2375, 2329, 2330, 2334, 2331, 2332],
[2317, 2391, 2425, 2429, 2464, 2468, 2476, 2497, 2517, 2531, 2533, 2530, 2518, 2515, 2490, 2501, 1854, 1849, 2445, 1914, 2457, 2498, 2501, 2474, 2337, 2401, 2406, 2400, 1294, 2327, 2355, 2333, 2352, 2318, 2371, 2330, 2335, 2330, 2332, 2333],
[2312, 2393, 2423, 2425, 2456, 2465, 2473, 2496, 2514, 2530, 2532, 2530, 2519, 2513, 2487, 2502, 1315, 2374, 2488, 1153, 2409, 2497, 2499, 2477, 2334, 2397, 2407, 2402, 1755, 2354, 2364, 2335, 2360, 2318, 2372, 2331, 2333, 2333, 2327, 2329],
[2312, 2396, 2429, 2429, 2455, 2462, 2473, 2499, 2514, 2530, 2535, 2531, 2518, 2515, 2486, 2504, 2372, 2441, 2492, 1806, 2449, 2501, 2499, 2479, 2443, 2410, 2408, 2404, 2451, 2391, 2368, 2333, 2354, 2312, 2368, 2332, 2329, 2328, 2336, 2329],
[2313, 2392, 2428, 2428, 2460, 2464, 2471, 2496, 2513, 2531, 2533, 2528, 2519, 2515, 2485, 2503, 1754, 1717, 2441, 1284, 2417, 2497, 2498, 2475, 2444, 2409, 2410, 2406, 2448, 2406, 2370, 2338, 2354, 2314, 2367, 2329, 2335, 2324, 2333, 2325],
[2309, 2393, 2428, 2429, 2459, 2464, 2477, 2497, 2511, 2528, 2532, 2528, 2518, 2514, 2489, 2503, 915, 2361, 2487, 913, 2398, 2496, 2497, 2473, 2440, 2410, 2410, 2398, 2446, 2409, 2371, 2335, 2352, 2325, 2369, 2333, 2336, 2334, 2331, 2324],
[2273, 2391, 2429, 2428, 2460, 2463, 2473, 2498, 2514, 2531, 2533, 2531, 2522, 2515, 2489, 2507, 1294, 2320, 2250, 959, 2399, 2495, 2496, 2477, 2446, 2405, 2410, 2404, 2411, 2394, 2369, 2338, 2354, 2321, 2368, 2325, 2333, 2331, 2332, 2329],
[2314, 2393, 2426, 2427, 2458, 2468, 2474, 2495, 2514, 2531, 2533, 2531, 2522, 2515, 2487, 2504, 1533, 2422, 2460, 913, 2395, 2495, 2495, 2478, 2441, 2409, 2410, 2402, 2450, 2403, 2372, 2337, 2324, 2311, 2364, 2325, 2336, 2335, 2325, 2324],
[2311, 2394, 2427, 2424, 2460, 2465, 2477, 2495, 2514, 2528, 2533, 2526, 2521, 2514, 2486, 2502, 1052, 2253, 2479, 914, 2396, 2495, 2484, 2476, 2274, 2399, 2408, 2404, 2176, 2388, 2368, 2334, 2328, 2314, 2366, 2329, 2333, 2333, 2336, 2327]])
print(arr)
def min_pooling(arr):
    x, y = arr.shape
    new_x, new_y = x//3 , y//2

    arr = np.min(arr.reshape(new_x, 3, y, 1), axis = (1,3))
    return arr
# sys.stdout = open('test.txt', 'w')
# print(min_pooling(arr))
# sys.stdout.close
print(len(arr))
min_pooling_arr = min_pooling(arr)
print(min_pooling_arr)
print(len(min_pooling_arr))

# print(min_pooling(min_pooling(min_pooling(min_pooling(arr)))))
# arr2 = np.arange(1,101).reshape(10,10)

# print(arr2)
# print(min_pooling(arr2))