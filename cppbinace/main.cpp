#include <fstream>
#include <iostream>
#include <string>
#include <curl/curl.h>
#include <nlohmann/json.hpp>
#include <chrono>
#include <thread>

// Use a global or static variable to track the last trade ID we saw
long long last_trade_id = 0;

size_t WriteCallback(void *contents, size_t size, size_t nmemb, std::string *userp)
{
    userp->append((char *)contents, size * nmemb);
    return size * nmemb;
}

void fetchData()
{
    CURL *curl = curl_easy_init();
    std::string readBuffer;

    if (curl)
    {
        // Add the 'fromId' parameter to the URL to only get NEW trades
        std::string url = "https://api-gcp.binance.com/api/v3/aggTrades?symbol=BNBETH&limit=500";
        if (last_trade_id > 0)
        {
            url += "&fromId=" + std::to_string(last_trade_id + 1);
        }

        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0L);
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

        if (curl_easy_perform(curl) == CURLE_OK)
        {
            auto data = nlohmann::json::parse(readBuffer);

            // If no new trades, just exit
            if (data.empty() || !data.is_array())
            {
                curl_easy_cleanup(curl);
                return;
            }

            std::ofstream csv("/app/cppbinace/build/output.csv", std::ios::app);
            std::ifstream checkEmpty("/app/cppbinace/build/output.csv");
            bool isEmpty = checkEmpty.peek() == std::ifstream::traits_type::eof();
            checkEmpty.close();

            if (isEmpty)
            {
                csv << "aggregate_trade_id,price,quantity,first_trade_id,last_trade_id,timestamp,buyer_is_maker,best_price_match\n";
            }

            for (auto &trade : data)
            {
                csv << trade["a"] << "," << trade["p"] << "," << trade["q"] << ","
                    << trade["f"] << "," << trade["l"] << "," << trade["T"] << ","
                    << trade["m"] << "," << trade["M"] << "\n";

                // Update the last_trade_id to the most recent one in this batch
                last_trade_id = trade["a"];
            }
            csv.close();
            std::cout << "Fetched " << data.size() << " new trades. Last ID: " << last_trade_id << std::endl;
        }
        curl_easy_cleanup(curl);
    }
}

int main()
{
    while (true)
    {
        fetchData();
        std::this_thread::sleep_for(std::chrono::seconds(10));
    }
    return 0;
}