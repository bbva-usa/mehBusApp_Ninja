package Database;

public class Routes {
    private int id;
    private String route;
    private String busNumber;
    private String address;
    private String pickupTime;
    private String dropoffTime;
    private Location geoLocation;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getRoute() {
        return route;
    }

    public void setRoute(String route) {
        this.route = route;
    }

    public String getBusNumber() {
        return busNumber;
    }

    public void setBusNumber(String busNumber) {
        this.busNumber = busNumber;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPickupTime() {
        return pickupTime;
    }

    public void setPickupTime(String pickupTime) {
        this.pickupTime = pickupTime;
    }

    public String getDropoffTime() {
        return dropoffTime;
    }

    public void setDropoffTime(String dropoffTime) {
        this.dropoffTime = dropoffTime;
    }

    public Location getGeoLocation() {
        return geoLocation;
    }

    public void setGeoLocation(Location geoLocation) {
        this.geoLocation = geoLocation;
    }
}
