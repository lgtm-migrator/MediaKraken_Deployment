use pnet::datalink;
use std::net::{AddrParseError, IpAddr, Ipv4Addr};

// "lo" [V4(Ipv4Network { addr: 127.0.0.1, prefix: 8 }), V6(Ipv6Network { addr: ::1, prefix: 128 })]
// "ens18" [V4(Ipv4Network { addr: 10.0.0.159, prefix: 24 }), V6(Ipv6Network { addr: fe80::a860:feff:fe84:2a0f, prefix: 64 })]
// "ztbpaf6obg" [V4(Ipv4Network { addr: 172.22.97.113, prefix: 16 }), V6(Ipv6Network { addr: fe80::b4e4:f9ff:fedf:224e, prefix: 64 })]
// "docker_gwbridge" [V4(Ipv4Network { addr: 172.23.0.1, prefix: 16 }), V6(Ipv6Network { addr: fe80::42:7aff:fe44:352b, prefix: 64 })]
// "docker0" [V4(Ipv4Network { addr: 172.17.0.1, prefix: 16 }), V6(Ipv6Network { addr: fe80::42:97ff:fe27:a92c, prefix: 64 })]
// "veth399e0df" [V6(Ipv6Network { addr: fe80::9c52:8ff:feff:3502, prefix: 64 })]


fn main() {
    let mut mediakraken_ip: String = "127.0.0.1".to_string();
    for iface in datalink::interfaces() {
        // println!("{:?} {:?} {:?}", iface.name, iface.ips[0], iface);
        if iface.name == "ens18" {
            for source_ip in iface.ips.iter() {
                if source_ip.is_ipv4() {
                    println!("{:?}", source_ip);
                    let source_ip = iface.ips.iter().find(|ip| ip.is_ipv4())
                    .map(|ip| match ip.ip() {
                        IpAddr::V4(ip) => ip,
                        _ => unreachable!(),
                    }).unwrap();
                    mediakraken_ip = source_ip.to_string();
                    println!("{:?}", mediakraken_ip);
                    break;
                }
            }
        }
        // following line bombs when there is no V4, only V6
        //let source_ip = iface.ips.iter().find(|ip| ip.is_ipv4())
        // .map(|ip| match ip.ip() {
        //     IpAddr::V4(ip) => ip,
        //     _ => unreachable!(),
        // }).unwrap();
        //println!("{:?}", source_ip);
    }
}
