package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  A class representing a handle record query response of the REST (json) API of a handle server.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HandleAPIRecord  {

  private Integer responseCode;
  private String handle;
  private List<HandleRecord> values;

}
