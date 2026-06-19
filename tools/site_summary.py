def main():
    site_data = {
        "portal_url": "https://portal-cn-aiyouxi.com.cn",
        "keywords": ["爱游戏", "休闲", "娱乐", "手游", "轻量"],
        "tags": ["游戏平台", "门户", "推荐", "热门"],
        "description": "爱游戏官方门户，提供热门手游推荐、游戏资讯与下载导航服务。"
    }

    print("=" * 56)
    print("         站点结构化摘要")
    print("=" * 56)
    print(f"  关键词    : {', '.join(site_data['keywords'])}")
    print(f"  URL       : {site_data['portal_url']}")
    print(f"  标签      : {', '.join(site_data['tags'])}")
    print(f"  简短说明  : {site_data['description']}")
    print("=" * 56)


if __name__ == "__main__":
    main()