package None;

import java.util.List;
import lombok.*;






/**
  A class representing a handle record in the same way as in the REST (json) API of a handle server.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HandleRecord  {

  private Integer ttl;
  private ZonedDateTime timestamp;
  private String type;

}
