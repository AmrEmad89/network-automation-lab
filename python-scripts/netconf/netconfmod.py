from ncclient import manager
from jinja2 import Template

def create_session(host, username, password):
    """Create and return a NETCONF session to the device."""
    connection = manager.connect(
        host=host,
        port=830,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': 'iosxe'},  # Cisco IOS XE device
        allow_agent=False,
        look_for_keys=False
    )
    return connection

def configure_loopback_interface(session, loopback_id, description, ip_address, subnet_mask):
    """Push Loopback interface configuration using an existing NETCONF session."""
    loopback_template = """
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <Loopback>
            <name>{{ loopback_id }}</name>
            <description>{{ description }}</description>
            <ip>
              <address>
                <primary>
                  <address>{{ ip_address }}</address>
                  <mask>{{ subnet_mask }}</mask>
                </primary>
              </address>
            </ip>
          </Loopback>
        </interface>
      </native>
    </config>
    """
    template = Template(loopback_template)
    config_xml = template.render(
        loopback_id=loopback_id,
        description=description,
        ip_address=ip_address,
        subnet_mask=subnet_mask
    )
    
    response = session.edit_config(target='running', config=config_xml)
    print("Loopback config response:")
    print(response)
