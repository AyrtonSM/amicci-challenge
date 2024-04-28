/** @type {import('next').NextConfig} */

const nextConfig = {
    webpack: (config) => {
        config.module.rules.push({
            test: /\.js$/,
            include: /utils/
        },{
            include: /components/
        });
        return config;
    },
};

export default nextConfig;
