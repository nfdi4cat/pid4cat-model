package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  A base class for handle-data classes that represent a handle record in the same way as in the REST (json) API of a handle server.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HandleRecord  {

  private ZonedDateTime timestamp;
  private Integer ttl;
  private String type;

}
